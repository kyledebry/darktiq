from operator import itemgetter


class Comm:
    def __init__(self, dmgr):
        super().__init__()

    def switch_clock(self, external):
        pass

    def load(self, kernel_library):
        pass

    def run(self):
        pass

    def serve(self, embedding_map, symbolizer, demangler):
        pass

    def check_ident(self):
        pass

    def get_log(self):
        return ""

    def clear_log(self):
        pass
