from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
PUBLIC = ROOT / 'public'

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split('?', 1)[0]
        if clean in ('/manifest.webmanifest','/sw.js','/manus-routes.json'):
            return str(PUBLIC / clean.lstrip('/'))
        return str(ROOT / clean.lstrip('/'))
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', 3000), Handler).serve_forever()
