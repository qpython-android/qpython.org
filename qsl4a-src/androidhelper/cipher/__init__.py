from json import dumps,loads
from base64 import b64encode as encode, b64decode as decode
from ..sl4a import Result
from ..__init__ import Android

class cipher:
	def __init__( this, sup ):
		p=__file__[:__file__.rfind('/')+1]
		for i in dir(this):
			if i[0] != '_':
				exec(f'sup.{i}=this.{i}')
				exec(f'cipher.{i}.__doc__=open("{p}{i}.txt").read()')
		this._rpc = sup._rpc
		this._write = sup._write
		this._flush = sup._flush
		this._readline = sup._readline
		this._sup = sup
		i=p[:p.rfind('/c')+1]
		cipher._init.__doc__ = open(f"{i}doc/cipherInit.txt").read().rsplit("\n",1)[0] + open(f"{p}_init.txt").read()
		sup.cipherInit = this._init

	def encryptString( self, srcString ):
		return self._rpc("encryptString", srcString)
	
	def decryptString( self, srcString ):
		return self._rpc("decryptString", srcString)
	
	def encryptStringToFile( self, srcString , dstFile ):
		return self._rpc("encryptStringToFile", srcString, dstFile)
	
	def decryptFileToString( self, srcFile ):
		return self._rpc("decryptFileToString", srcFile)
	
	def encryptFile( self, srcFile, dstFile ):
		return self._rpc("encryptFile", srcFile, dstFile)
	
	def decryptFile( self, srcFile, dstFile ):
		return self._rpc("decryptFile", srcFile, dstFile)
	
	def encryptBytes( self, srcBytes ):
		return self._brpc("encryptString", encode( srcBytes ).decode())
	
	def decryptBytes( self, srcBytes ):
		return self._brpc("decryptString", encode( srcBytes ).decode())
	
	def encryptBytesToFile( self, srcBytes , dstFile ):
		return self._rpc("encryptStringToFile", encode( srcBytes ).decode(), dstFile)
	
	def decryptFileToBytes( self, srcFile ):
		return self._brpc("decryptFileToString", srcFile)
	
	def _brpc( self, method, *args ):
		self._write( dumps({
			'id': self._sup._id,
			'method': method,
			'params': args
		}) + '\n' )
		self._flush()
		self._sup._id += 1
		result = loads( self._readline() )
		if result['error'] is not None:
			print(result['error'])
		else:
			result['result'] = decode( result['result'] )
		return Result( result['id'], result['result'], result['error'] )
	
	def _init( self, key, algorithm = "AES/CBC/PKCS5Padding", encodingFormat = "", initialVector = ""):
		if isinstance( key ,( bytes, bytearray )):
			key = encode(key).decode()
		if isinstance( initialVector ,( bytes, bytearray )):
			initialVector = encode(initialVector).decode()
		return self._rpc( "cipherInit", key, algorithm, encodingFormat, initialVector )

#by 乘着船 2021-2025
