#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

# Map of corrupted sequences -> correct characters
replacements = {
    'â€"': '—',
    'â€™': '\u2019',
    'â€˜': '\u2018',
    'â€œ': '"',
    'â€': '"',
    'â€¢': '•',
    "â†'": "→",
    # Corrupted emojis: each corrupted 4-byte emoji appears as a 3-char mojibake
    # We fix them by re-encoding the mojibake latin1 -> utf-8
}

# First fix simple text replacements
for bad, good in replacements.items():
    text = text.replace(bad, good)

# Fix emoji mojibake by detecting the pattern: latin1-encoded bytes that are actually utf-8
# The mojibake happens because the file was double encoded.
# We detect sequences of chars in range 0xC0-0xFF followed by 0x80-0xBF equivalents
def fix_mojibake(s):
    result = []
    i = 0
    chars = list(s)
    while i < len(chars):
        c = chars[i]
        # Detect 4-byte utf-8 sequence encoded as latin1 (starts with 0xF0)
        if ord(c) == 0xC3 and i + 1 < len(chars):
            # 2-byte sequence
            try:
                b = bytes([ord(c) & 0xFF, ord(chars[i+1]) & 0xFF])
                decoded = b.decode('utf-8')
                result.append(decoded)
                i += 2
                continue
            except:
                pass
        # Detect 4-byte emoji (F0 9F ...)
        if ord(c) == 0xF0 and i + 3 < len(chars):
            try:
                b = bytes([ord(chars[i]) & 0xFF, ord(chars[i+1]) & 0xFF,
                           ord(chars[i+2]) & 0xFF, ord(chars[i+3]) & 0xFF])
                decoded = b.decode('utf-8')
                result.append(decoded)
                i += 4
                continue
            except:
                pass
        result.append(c)
        i += 1
    return ''.join(result)

# Instead: just do a direct byte-level re-decoding approach
# Read raw bytes and decode properly
with open('index.html', 'rb') as f:
    raw = f.read()

# Try to fix double-encoding artifacts
# The file is UTF-8 but was saved as latin1 then re-read as UTF-8
# Common pattern: UTF-8 bytes were interpreted as latin1 string, then saved as UTF-8 again
# To fix: decode as latin1, then encode as latin1 bytes, then decode as utf-8
try:
    fixed = raw.decode('utf-8', errors='replace')
    # Check for mojibake signature (c3/c2 sequences indicating double-encoded UTF-8)
    if 'Ã' in fixed or 'â€' in fixed or 'ð' in fixed:
        # Try to recover: re-encode each char as latin1 byte, collect bytes, decode as utf-8
        recovered_bytes = bytearray()
        for ch in fixed:
            try:
                recovered_bytes += ch.encode('latin-1')
            except:
                # Character not in latin-1, keep as utf-8 bytes
                recovered_bytes += ch.encode('utf-8')
        try:
            fixed = recovered_bytes.decode('utf-8')
        except:
            # Some parts still fail, do mixed approach
            fixed = recovered_bytes.decode('utf-8', errors='replace')
    
    # Now do string replacements for any remaining issues
    fixed = fixed.replace('â\x80\x94', '—')
    fixed = fixed.replace('â€"', '—')
    fixed = fixed.replace('â€™', '\u2019')
    fixed = fixed.replace('â€¢', '•')
    
except Exception as e:
    print(f"Error: {e}")
    fixed = raw.decode('utf-8', errors='replace')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed)

# Verify
with open('index.html', 'r', encoding='utf-8') as f:
    verify = f.read()

import_count = verify.count('â€"') + verify.count('ð') + verify.count('Ã')
print(f"Remaining mojibake sequences: {import_count}")
print("Done!")
