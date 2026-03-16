try:
    from requests import request
except:
    error=Exception('Please pip install apigptcloud .')
    def request(*a,**b):raise error
    print(error)

from time import sleep
from .sl4a import Result
from .__init__ import Android
from os.path import basename,splitext,abspath
from os import environ
from traceback import format_exc
import configparser

def read_conf_file(conf_file_path, section, key):
    # 创建配置解析器对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read(conf_file_path)
    # 获取指定 section 下的指定 key 的值
    value = config.get(section, key)
    return value

try:
    keyOfSpeech = read_conf_file(environ['ANDROID_PUBLIC']+"/files/apigpt.conf", "speech", "speech_key")
except:
    keyOfSpeech = "MWYwZWVmNWQ0MGRiNGE5ZjBmZjFiNTUxMjVlMGNiYWE="

headers = {
    'accept': 'application/json',
    "Authorization": "Bearer "+keyOfSpeech
}

urlPref = 'https://ai.pgpt.cloud/v1/speech/'

defaultLanguage = {
  'en':'en-US',
  'zh':'zh-CN'
}

defaultVoice = {
  'en':'en-US-JennyNeural',
  'zh':'zh-CN-XiaoxiaoNeural'
}

class pgptai:

    def __init__( this, sup ):
        for i in dir(this):
            if i[0] != '_':
                exec(f'pgptai.{i}.__doc__=Android.{i}.__doc__\nsup.{i}=this.{i}')
        this._rpc = sup._rpc
        this._write = sup._write
        this._flush = sup._flush
        this._readline = sup._readline
        this._sup = sup

    def speechToText(self, RecordSecond = 10, AmrFile = None, Language = None):
        if not AmrFile:
            AmrFile = environ['TMP']+'/tmp.amr'
        AmrFile = abspath(AmrFile)
        if not RecordSecond:
            self._sup._id += 1
        else:
            response = self._rpc('recorderStartMicrophone',AmrFile)
            if response.error:
                return Result(self._sup._id,None,'Record Start : '+response.error)
            sleep(RecordSecond)
            response = self._rpc('recorderStop')
            if response.error:
                return Result(self._sup._id,None,'Record Stop : '+response.error)
        url = urlPref + 'speech2text'
        if not Language:
            Language = defaultLanguage[environ['LANG'][:2]]
        params = {
            'lang': Language,
        }
        files = [
          ( 'audio', 
          (
            basename(AmrFile),
            open(AmrFile,'rb'),
            'audio/'+splitext(AmrFile)[1][1:]
        ))]
        id = self._sup._id
        try:
            response = request("POST", url, headers=headers, params=params, files=files)
        except:
            return Result(id,None,format_exc())
        status_code=response.status_code
        content=str(response.content,'utf-8')
        try:
            content=eval(content)
        except:
            pass
        if status_code!=200:
            try:
                content=content['error']
            except:
                pass
            return Result(id,None,content)
        else:
            return Result(id,content['text'],None)

    def textToSpeech(self, Text, AutoPlay = True, WavFile = None, VoiceName = None):
        if not VoiceName:
            VoiceName = defaultVoice[environ['LANG'][:2]]
        url = urlPref + 'text2speech'
        data = {
            'voice_name': VoiceName,
            'text': Text,
        }
        id = self._sup._id
        try:
            response = request('POST', url, headers=headers, json=data)
        except:
            return Result(id,None,format_exc())
        status_code=response.status_code
        content=str(response.content,'utf-8')
        try:
            content=eval(content)
        except:
            pass
        if status_code!=200:
            try:
                content=content['error']
            except:
                pass
            return Result(id,None,content)
        else:
            if not WavFile:
                WavFile = environ['TMP']+'/tmp.wav'
            try:
                url=content['url']
                wav=request('GET',url).content
                open(WavFile,'wb').write(wav)
                content['WavFile']=WavFile
                if AutoPlay:
                    self._rpc('mediaPlay',WavFile)
                id = self._sup._id
                self._sup._id += 1
                return Result(id,content,None)
            except:
                id = self._sup._id
                self._sup._id += 1
                return Result(id,None,str(content)+'\n'+format_exc())

# by 乘着船 @ Bilibili at 2023
