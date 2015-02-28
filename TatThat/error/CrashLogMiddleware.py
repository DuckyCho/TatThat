import traceback
import socket
import warnings
import hashlib
from datetime import datetime

class CrashLogMiddleware(object):
    def process_exception(self, request, exception):
        server_name = socket.gethostname()
        tb_text     = traceback.format_exc()
        class_name  = exception.__class__.__name__
        checksum    = hashlib.md5.new(tb_text).hexdigest()

        try:
            lLogFilePath = "/Users/choducky/AppLog.log"

            lLogFile = open(lLogFilePath, "a")
            lLogFile.write("==== " + str(datetime.now()) + "=====================================\n")
            lLogFile.write(getattr(exception, "message", "") + "\n")
            lLogFile.write("Url: %s\n" % request.build_absolute_uri())
            lLogFile.write("Server: %s\n" % server_name)
            lLogFile.write(tb_text + "\n")
            lLogFile.flush()
            lLogFile.close()
        except Exception, exc:
            warnings.warn(unicode(exc))