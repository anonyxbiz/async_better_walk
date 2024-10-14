# ./async_better_walk.py
from subprocess import Popen, PIPE
from asyncio import run, to_thread as to
from re import findall, DOTALL
from os.path import exists
from logging import Formatter, StreamHandler, DEBUG, getLogger

class GreenFormatter(Formatter):
    def format(app, record):
        log_message = super().format(record)
        return log_message
        
logger = getLogger("logger")
logger.setLevel(DEBUG)
ch = StreamHandler()
formatter = GreenFormatter("%(message)s")

ch.setFormatter(formatter)
logger.addHandler(ch)

p = logger.info

class Os(object):
    read_size = 256
    dir = None
    @classmethod
    async def init(app, **kwargs):
        app = app()
        app.__dict__.update(kwargs)
        return app
    
    async def walk(app, bytes=None, chunks=""):
        if bytes: app.read_size = bytes
        async for chunk in app.bash("find %s -type f" % app.dir):
            if chunk:
                chunks += chunk
            if "\n" in chunks:
                for file in (files := chunks.split("\n")):
                    if await to(exists, file):
                        chunks = chunks.replace(file + "\n", "")
                        yield file
                    
    async def bash(app, cmd):
        try:
            process = await to(Popen, cmd, stdout=PIPE, stderr=PIPE, shell=True, text=True)
            
            if await to(process.wait,) != 0:
                while (chunk := await to(process.stderr.read,app.read_size)):
                    yield chunk
            else:
                while (chunk := await to(process.stdout.read,app.read_size)):
                    yield chunk
                
        except Exception as e:
            p(str(e))
        
if __name__=="__main__":                       
    dir = "."
    async def m():
        app = await Os.init(dir=dir)
        
        async for file in app.walk(1024):
            p(file)
    
    run(m())