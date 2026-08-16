from pathlib import Path
import re

ARTIFACTS = [
    "MAXESS-RESULTS-FINAL-GROOVE.html",
    "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    "MAXESS-RESULTS-10-GROOVE.html",
    "MAXESS-RESULTS-GROOVE-EMBED.html",
    "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

MARKER = "MAXESS_RESULT_10_10_BOOTSTRAP"

BOOTSTRAP = '''<!-- MAXESS_RESULT_10_10_BOOTSTRAP -->
<script>
(function () {
  "use strict";
  var result = null;
  try {
    var encoded = new URLSearchParams(window.location.search).get("result");
    if (encoded) {
      var normalized = encoded.replace(/-/g, "+").replace(/_/g, "/");
      while (normalized.length % 4) normalized += "=";
      var binary = atob(normalized);
      var bytes = new Uint8Array(binary.length);
      for (var i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
      result = JSON.parse(new TextDecoder().decode(bytes));
    }
  } catch (error) {
    console.warn("MAXESS_RESULT query payload could not be decoded; using bootstrap fallback.", error);
  }
  window.MAXESS_RESULT = result || {
    resonance: 10.10,
    signature: "LIVING",
    naya: "AWAKENED",
    groove: "MAXIMAL",
    status: "FULL_ACTIVATION",
    timestamp: new Date().toISOString()
  };
  console.log("%cMAXESS 10.10 INITIALIZED", "color:#00ffcc; font-size:18px; font-weight:bold;");
})();
</script>
'''

changed = 0
for filename in ARTIFACTS:
    path = Path(filename)
    if not path.exists():
        continue
    source = path.read_text(encoding="utf-8")
    if MARKER in source:
        continue
    match = re.search(r"<head(?:\s[^>]*)?>", source, flags=re.I)
    if match:
        patched = source[:match.end()] + "\n" + BOOTSTRAP + source[match.end():]
    else:
        patched = BOOTSTRAP + source
    path.write_text(patched, encoding="utf-8")
    changed += 1
    print(f"INJECTED: {filename}")

if changed == 0:
    print("No artifact required a new bootstrap injection.")
