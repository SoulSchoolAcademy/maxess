#!/usr/bin/env python3
"""Normalize generated Results artifacts for readable, verifiable delivery."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
FILES=[ROOT/'MAXESS-RESULTS-FINAL-GROOVE.html',ROOT/'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-10-GROOVE.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED-9.95.html']

def format_style(match):
    body=match.group(1)
    body=re.sub(r';(?=[^\n])',';\n',body)
    body=re.sub(r'\{(?=[^\n])','{\n',body)
    body=re.sub(r'\}(?=[^\n])','}\n',body)
    return '<style>'+body+'</style>'

def format_markup(text):
    text=re.sub(r'>\s*<','>\n<',text)
    text=re.sub(r'<style(?:\s[^>]*)?>(.*?)</style>',format_style,text,flags=re.I|re.S)
    text=re.sub(r'</script>','\n</script>\n',text,flags=re.I)
    return text.strip()+'\n'

for path in FILES:
    if not path.exists(): raise SystemExit(f'Missing artifact: {path}')
    data=format_markup(path.read_text(encoding='utf-8'))
    path.write_text(data,encoding='utf-8')
    print(f'{path.name}: {len(data.splitlines())} lines / {len(data.encode())} bytes')
