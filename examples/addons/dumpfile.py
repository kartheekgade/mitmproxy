import random
from typing import BinaryIO

from mitmproxy import http
from mitmproxy import io
from mitmproxy import ctx

from typing import Optional

class Writer:
        
    def load(self, loader):
        loader.add_option(
            name="path",
            typespec=Optional[str],
            default=None,
            help="Specify a path for the mitmproxy dump file"
        )

        if ctx.options.path:
            self.f: BinaryIO = open(ctx.options.path,"wb")
        else:
            self.f: BinaryIO = open("dump.txt","wb")

        self.w = io.FlowWriter(self.f)

    def response(self, flow: http.HTTPFlow) -> None: 
        if random.choice([True, False]):
            self.w.add(flow)

    def done(self):
        self.f.close()

addons = [Writer()]   