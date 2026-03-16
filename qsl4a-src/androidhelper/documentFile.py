from base64 import b64encode as encode, b64decode as decode
from .sl4a import Result
from .__init__ import Android
import os
sdcard = os.environ['EXTERNAL_STORAGE']

class documentFile:
    def __init__( this, sup ):
        for i in dir(this):
            if i[0] != '_':
                exec(f'sup.documentFile{i}=this.{i}')
        this._rpc = sup._rpc
        this._write = sup._write
        this._flush = sup._flush
        this._readline = sup._readline
        this._sup = sup
        sup.documentFileShowOpen = sup.documentTreeShowOpen = this._TreeShowOpen
        sup.documentFileMoveTo = this.RenameTo
        sup.documentFileMkdirs = this.Mkdir
        sup.documentFileWriteTo = this.OutputStream
        sup.documentFileReadFrom = this.InputStream

    def Mkdir( self, Dir ):
        '''
documentFileMkdir( Dir )
  Make New Directory(s)
  documentFileMkdirs is the same as documentFileMkdir .
  Return True if Success .
'''
        return self._rpc("documentFileMkdir", Dir)
    
    def Delete( self, FileOrTree ):
        '''
documentFileDelete( FileOrTree )
  Return True if Success .
'''
        return self._rpc("documentFileDelete", FileOrTree)
    
    def RenameTo( self, Src, Dest ):
        '''
documentFileRenameTo( Src, Dest )
  documentFileMoveTo is the same as documentFileRenameTo
  Move or Rename Tree or File .
  Return True if Success .
'''
        return self._rpc("documentFileRenameTo", Src, Dest )
    
    def Copy( self, SrcFileOrTree, DestFileOrTree ):
        '''
documentFileCopy( SrcFileOrTree, DestFileOrTree )
  Return None .
'''
        return self._rpc("documentFileCopy", SrcFileOrTree, DestFileOrTree )

    def ListFiles( self, Folder ):
        '''
documentFileListFiles( Folder )
  Return List of Files of the Folder .
'''
        return self._rpc("documentFileListFiles", Folder )
    
    def InputStream( self, srcFile, EncodingFormat = "", skip = None, length = None ):
        '''
documentFileInputStream( srcFile, EncodingFormat = "", skip = None, length = None )
documentFileReadFrom is the same as documentFileInputStream .
If EncodingFormat is omitted ( empty default ) , this function will return Bytes ;
If EncodingFormat is Base64 , this function will return Base64 String ;
If EncodingFormat is UTF-8 or GBK etc , this function will return Normal String .
If skip is None default, skip == 0 (start of srcFile) , otherwise skip bytes from srcFile's head,
If length is None default, length means rest of srcFile, read length bytes from skip place .
'''
        if EncodingFormat:
            if EncodingFormat.upper()=='BASE64':
                EncodingFormat=''
            return self._rpc("documentFileInputStream", srcFile, EncodingFormat, skip, length)
        else:
            r=self._rpc("documentFileInputStream", srcFile, '', skip, length)
            return Result(r.id,decode(r.result),r.error)
    
    def OutputStream( self, destFile, src, EncodingFormat = "", append = None ):
        '''
documentFileOutputStream( destFile, src, EncodingFormat = "", append = None )
documentFileWriteTo is the same as documentFileOutputStream .
If EncodingFormat is omitted (empty default) , src will be Bytes ;
If EncodingFormat is Base64 , src will be Base64 String ;
If EncodingFormat is UTF-8 or GBK etc , src will be Normal String ;
When a destFile exists, if append is True, append content to the end of the destFile, if append is False or None, overwrite the original destFile .
This Function always return None .
'''
        if EncodingFormat:
            if EncodingFormat.upper()=='BASE64':
                EncodingFormat=''
            return self._rpc("documentFileOutputStream", destFile, src, EncodingFormat, append)
        else:
            return self._rpc("documentFileOutputStream", destFile, encode( src ).decode(), '', append)

    def GetUri(self, path, isDirectory = None):
        '''
documentFileGetUri(path, isDirectory = None)
Return $URI according to the specific path .
    path (String)
    isDirectory (Boolean Optional) :
        True  - must     be         a directory , create an empty folder         if not exist ;
        False - must not be         a directory , create an empty file           if not exist ;
        None  - don't know if it is a directory , create nothing and return None if not exist .
'''
        return self._rpc("documentFileGetUri", path, isDirectory )

    def IsDirectory(self, path):
        '''
documentFileIsDirectory(path)
Return a path is a directory ,
    if path not exists or not available , return None .
    path (String)
'''
        return self._rpc("documentFileIsDirectory", path )

    def IsFile(self, path):
        '''
documentFileIsFile(path)
Return a path is a file ,
    if path not exists or not available , return None .
    path (String)
'''
        return self._rpc("documentFileIsFile", path )

    def Exists(self, path):
        '''
documentFileExists(path)
Return a path is exists ,
    path (String)
'''
        return self._rpc("documentFileExists", path )

    def LastModified(self, path):
        '''
documentFileLastModified(path)
Return a path's Last Modified time,
    if path not exists or not available , return 0 .
    path (String)
'''
        return self._rpc("documentFileLastModified", path )

    def Length(self, path):
        '''
documentFileLength(path)
Return a path's file size,
    if path not exists or not available , return 0 .
    path (String)
'''
        return self._rpc("documentFileLength", path )

    def GetStat(self, path):
        '''
documentFileGetStat(path)
Return a dict of file length , last modified and file can read/write ,
    if path not exists or not available , return None .
    path (String)
'''
        return self._rpc("documentFileGetStat", path )

    def _TreeShowOpen( self, rootPath = sdcard ):
        return self._rpc("documentTreeShowOpen", rootPath )

_i='"content://com.android.externalstorage.documents/<ContentPaths>"'
_d=documentFile.GetUri
_d.__doc__=_d.__doc__.replace('$URI',_i)
documentFile._TreeShowOpen.__doc__=Android.documentTreeShowOpen.__doc__.replace('/sdcard',sdcard).replace('$URI',_i)
_d='Use This Function to Read/Write Media Storage Device or "/sdcard/Android/<subPath>" .'.replace('/sdcard',sdcard)
for _i in dir(documentFile):
    if _i[0]!='_':
        exec('documentFile.%s.__doc__+=_d'%_i)
del _d,_i

#by 乘着船 2021-2023