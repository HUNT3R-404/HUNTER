# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))