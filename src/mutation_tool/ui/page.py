# ruff: noqa: E501

# Single-page HTML application with embedded CSS and JavaScript for mutation testing UI
INDEX_HTML = r"""
<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mutation Lab</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Public+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --paper: oklch(98.2% 0.008 80);
      --paper-soft: oklch(96.5% 0.012 80);
      --ink: oklch(22% 0.025 50);
      --ink-soft: oklch(42% 0.02 50);
      --ink-faint: oklch(62% 0.018 60);
      --rule: oklch(88% 0.012 80);
      --rule-soft: oklch(93% 0.01 80);

      --accent: oklch(46% 0.14 28);
      --accent-strong: oklch(38% 0.16 28);
      --accent-soft: oklch(94% 0.04 28);

      --good: oklch(48% 0.13 145);
      --good-soft: oklch(94% 0.04 145);
      --warn: oklch(58% 0.14 65);
      --warn-soft: oklch(95% 0.05 65);
      --info: oklch(50% 0.12 230);
      --info-soft: oklch(94% 0.04 230);

      --font-display: "Fraunces", "Iowan Old Style", Georgia, serif;
      --font-body: "Public Sans", system-ui, sans-serif;
      --font-mono: "JetBrains Mono", ui-monospace, monospace;

      --measure: 64ch;
    }

    *, *::before, *::after { box-sizing: border-box; }

    html { background: var(--paper); }

    body {
      margin: 0;
      min-height: 100vh;
      font-family: var(--font-body);
      font-size: 17px;
      line-height: 1.65;
      color: var(--ink);
      background: var(--paper);
      -webkit-font-smoothing: antialiased;
      font-feature-settings: "ss01", "cv02";
    }

    a { color: var(--accent); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }

    /* Page frame */
    .page {
      max-width: 880px;
      margin: 0 auto;
      padding: clamp(28px, 5vw, 56px) clamp(20px, 5vw, 64px) 120px;
    }

    /* Top bar */
    .top {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--rule);
      margin-bottom: clamp(36px, 6vw, 64px);
    }

    .brand {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.05rem;
      letter-spacing: -0.01em;
      color: var(--ink);
      font-variation-settings: "opsz" 14;
    }

    .brand .mark {
      display: inline-block;
      width: 8px;
      height: 8px;
      background: var(--accent);
      margin-right: 10px;
      transform: translateY(-2px);
    }

    .lang {
      display: inline-flex;
      gap: 14px;
      font-family: var(--font-body);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }
    .lang button {
      appearance: none;
      background: transparent;
      border: 0;
      padding: 4px 2px;
      font: inherit;
      color: var(--ink-faint);
      cursor: pointer;
      border-bottom: 1px solid transparent;
    }
    .lang button.active { color: var(--ink); border-bottom-color: var(--accent); }
    .lang button:hover { color: var(--ink); }

    /* Title */
    h1.title {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: clamp(2.8rem, 6.5vw, 4.4rem);
      line-height: 1;
      letter-spacing: -0.035em;
      margin: 0 0 18px;
      max-width: 14ch;
      color: var(--ink);
      font-variation-settings: "opsz" 144;
    }

    h1.title em {
      font-style: italic;
      font-weight: 500;
      color: var(--accent);
    }

    .lede {
      font-family: var(--font-display);
      font-style: italic;
      font-weight: 400;
      font-size: clamp(1.15rem, 2.2vw, 1.4rem);
      line-height: 1.45;
      color: var(--ink-soft);
      max-width: 48ch;
      margin: 0 0 12px;
      font-variation-settings: "opsz" 36;
    }

    .intro-body {
      max-width: var(--measure);
      color: var(--ink-soft);
      font-size: 1.02rem;
      margin: 0;
    }

    /* Section */
    section.step {
      margin-top: clamp(48px, 7vw, 80px);
      padding-top: clamp(28px, 4vw, 40px);
      border-top: 1px solid var(--rule);
      display: grid;
      grid-template-columns: 96px minmax(0, 1fr);
      gap: clamp(16px, 3vw, 36px);
      align-items: start;
    }

    .step-marker {
      font-family: var(--font-display);
      font-style: italic;
      font-weight: 400;
      font-size: clamp(3rem, 6vw, 4.5rem);
      line-height: 1;
      color: var(--accent);
      font-variation-settings: "opsz" 144;
      letter-spacing: -0.04em;
    }

    .step-marker::after { content: "."; color: var(--ink-faint); }

    .step-body { min-width: 0; }

    h2.step-title {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: clamp(1.75rem, 3.5vw, 2.4rem);
      line-height: 1.1;
      letter-spacing: -0.025em;
      margin: 0 0 14px;
      color: var(--ink);
      font-variation-settings: "opsz" 72;
    }

    .step-desc {
      max-width: var(--measure);
      color: var(--ink-soft);
      font-size: 1rem;
      margin: 0 0 28px;
    }

    .step-desc + .step-controls { margin-top: 0; }

    /* Mode picker */
    .mode-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 28px;
    }

    .mode {
      position: relative;
      padding: 18px 20px 16px;
      border: 1px solid var(--rule);
      background: var(--paper);
      cursor: pointer;
      transition: border-color 0.18s, background 0.18s;
    }
    .mode:hover { border-color: var(--ink-faint); }
    .mode input[type=radio] { position: absolute; opacity: 0; pointer-events: none; }
    .mode.active {
      border-color: var(--accent);
      background: var(--accent-soft);
    }

    .mode-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }

    .mode-name {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.18rem;
      color: var(--ink);
      letter-spacing: -0.015em;
    }

    .mode-marker {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      border: 1.5px solid var(--ink-faint);
      background: var(--paper);
      position: relative;
      flex-shrink: 0;
    }
    .mode.active .mode-marker { border-color: var(--accent); }
    .mode.active .mode-marker::after {
      content: "";
      position: absolute;
      inset: 3px;
      border-radius: 50%;
      background: var(--accent);
    }

    .mode-desc {
      font-size: 0.92rem;
      color: var(--ink-soft);
      margin: 0;
    }

    /* Field */
    .panel.hidden { display: none; }

    .field {
      display: grid;
      gap: 6px;
      margin-bottom: 18px;
    }
    .field:last-child { margin-bottom: 0; }

    .field-label {
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 0.92rem;
      color: var(--ink);
      letter-spacing: -0.005em;
    }

    .field-hint {
      font-size: 0.86rem;
      color: var(--ink-faint);
      margin: 0;
    }

    .field-hint code, .inline-code {
      font-family: var(--font-mono);
      font-size: 0.88em;
      background: var(--paper-soft);
      padding: 1px 6px;
      border: 1px solid var(--rule);
      color: var(--ink);
    }

    input[type=text], input[type=number], select {
      width: 100%;
      padding: 12px 14px;
      border: 1px solid var(--rule);
      background: var(--paper);
      font-family: var(--font-body);
      font-size: 1rem;
      color: var(--ink);
      border-radius: 6px;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    input:focus, select:focus {
      outline: 0;
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-soft);
    }

    select[multiple] {
      padding: 6px;
      min-height: 110px;
      font-family: var(--font-mono);
      font-size: 0.88rem;
    }
    select[multiple] option { padding: 6px 8px; }

    /* Counter */
    .counter {
      display: inline-flex;
      align-items: stretch;
      border: 1px solid var(--rule);
      border-radius: 8px;
      overflow: hidden;
      background: var(--paper);
    }

    .counter button {
      appearance: none;
      background: var(--paper);
      border: 0;
      width: 48px;
      font-family: var(--font-display);
      font-weight: 500;
      font-size: 1.4rem;
      color: var(--ink);
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }
    .counter button:hover { background: var(--accent); color: var(--paper); }
    .counter button:first-child { border-right: 1px solid var(--rule); }
    .counter button:last-child { border-left: 1px solid var(--rule); }

    .counter input {
      width: 88px;
      text-align: center;
      border: 0;
      background: transparent;
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.45rem;
      color: var(--ink);
      padding: 12px 0;
      border-radius: 0;
      font-variant-numeric: tabular-nums;
    }
    .counter input::-webkit-inner-spin-button,
    .counter input::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }

    .counter-aside {
      display: inline-block;
      margin-left: 16px;
      font-size: 0.92rem;
      color: var(--ink-faint);
      vertical-align: middle;
    }

    .counter-wrap {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 4px 16px;
    }

    /* Advanced */
    details.advanced {
      margin-top: 28px;
      border-top: 1px dashed var(--rule);
      padding-top: 18px;
    }
    details.advanced > summary {
      cursor: pointer;
      list-style: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-body);
      font-weight: 500;
      font-size: 0.94rem;
      color: var(--ink-soft);
    }
    details.advanced > summary:hover { color: var(--accent); }
    details.advanced > summary::-webkit-details-marker { display: none; }
    details.advanced > summary::before {
      content: "+";
      display: inline-block;
      width: 16px;
      text-align: center;
      font-family: var(--font-display);
      font-weight: 500;
      color: var(--accent);
    }
    details.advanced[open] > summary::before { content: "\2013"; }

    .advanced-content {
      margin-top: 20px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px 24px;
    }
    .advanced-content .field-wide { grid-column: 1 / -1; }

    .toggle {
      grid-column: span 1;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 0;
      cursor: pointer;
      border-top: 1px solid var(--rule-soft);
    }
    .toggle input[type=checkbox] {
      appearance: none;
      width: 18px;
      height: 18px;
      border: 1.5px solid var(--ink-faint);
      background: var(--paper);
      cursor: pointer;
      margin: 0;
      flex-shrink: 0;
      margin-top: 2px;
      border-radius: 3px;
      position: relative;
    }
    .toggle input[type=checkbox]:checked {
      background: var(--accent);
      border-color: var(--accent);
    }
    .toggle input[type=checkbox]:checked::after {
      content: "";
      position: absolute;
      left: 4px; top: 0;
      width: 5px; height: 10px;
      border: solid var(--paper);
      border-width: 0 2px 2px 0;
      transform: rotate(45deg);
    }
    .toggle-text { display: grid; gap: 2px; }
    .toggle-label { font-weight: 600; font-size: 0.95rem; color: var(--ink); }
    .toggle-hint { font-size: 0.85rem; color: var(--ink-faint); }

    /* Run button */
    .run-row {
      margin-top: 36px;
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .run-btn {
      appearance: none;
      background: var(--ink);
      color: var(--paper);
      border: 0;
      padding: 16px 28px;
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 1.02rem;
      letter-spacing: -0.005em;
      cursor: pointer;
      border-radius: 8px;
      transition: background 0.18s, transform 0.1s;
      display: inline-flex;
      align-items: center;
      gap: 12px;
    }
    .run-btn:hover:not(:disabled) { background: var(--accent); }
    .run-btn:active:not(:disabled) { transform: translateY(1px); }
    .run-btn:disabled { background: var(--rule); color: var(--ink-faint); cursor: not-allowed; }
    .run-btn .arrow {
      font-family: var(--font-display);
      font-weight: 500;
      font-size: 1.2rem;
    }

    .run-hint {
      font-size: 0.88rem;
      color: var(--ink-faint);
      font-style: italic;
      font-family: var(--font-display);
    }

    /* Result area */
    .result-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
      gap: clamp(24px, 4vw, 48px);
      align-items: start;
    }

    .score-stack { min-width: 0; }

    .score-label {
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 0.85rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--ink-soft);
      margin: 0 0 6px;
    }

    .score-value {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: clamp(4.5rem, 12vw, 8rem);
      line-height: 0.88;
      letter-spacing: -0.055em;
      color: var(--ink);
      font-variant-numeric: tabular-nums;
      font-variation-settings: "opsz" 144;
    }
    .score-value .unit {
      font-size: 0.28em;
      vertical-align: top;
      color: var(--accent);
      margin-left: 6px;
      font-weight: 500;
    }

    .score-narrate {
      margin: 14px 0 0;
      font-family: var(--font-display);
      font-style: italic;
      font-size: 1.15rem;
      color: var(--ink-soft);
      max-width: 38ch;
      line-height: 1.45;
    }
    .score-narrate strong { color: var(--ink); font-style: normal; font-weight: 600; }

    .breakdown {
      display: grid;
      gap: 0;
    }

    .bd-row {
      display: grid;
      grid-template-columns: 22px 1fr auto;
      align-items: baseline;
      gap: 14px;
      padding: 14px 0;
      border-bottom: 1px solid var(--rule);
    }
    .bd-row:first-child { border-top: 1px solid var(--rule); }
    .bd-glyph {
      font-family: var(--font-mono);
      font-weight: 500;
      text-align: center;
    }
    .bd-name {
      font-family: var(--font-body);
      font-weight: 500;
      font-size: 0.96rem;
      color: var(--ink);
    }
    .bd-detail {
      font-size: 0.84rem;
      color: var(--ink-faint);
      display: block;
      font-weight: 400;
      margin-top: 2px;
    }
    .bd-value {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.35rem;
      font-variant-numeric: tabular-nums;
      color: var(--ink);
    }

    .bd-row.good .bd-glyph { color: var(--good); }
    .bd-row.bad .bd-glyph { color: var(--accent); }
    .bd-row.warn .bd-glyph { color: var(--warn); }
    .bd-row.info .bd-glyph { color: var(--info); }
    .bd-row.bad .bd-value { color: var(--accent-strong); }

    /* Status strip */
    .status-strip {
      margin-top: 36px;
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 14px 18px;
      border: 1px solid var(--rule);
      background: var(--paper-soft);
      border-radius: 8px;
      flex-wrap: wrap;
    }
    .status-dot {
      width: 10px; height: 10px;
      background: var(--ink-faint);
      flex-shrink: 0;
      border-radius: 50%;
    }
    .status-dot.running { background: var(--accent); animation: pulse 1.2s ease-in-out infinite; }
    .status-dot.completed { background: var(--good); }
    .status-dot.failed { background: var(--accent-strong); }
    @keyframes pulse { 50% { opacity: 0.4; transform: scale(1.2); } }

    .status-label {
      font-weight: 600;
      font-size: 0.92rem;
      color: var(--ink);
      letter-spacing: -0.005em;
    }
    .status-msg {
      color: var(--ink-soft);
      font-size: 0.92rem;
      flex: 1;
      min-width: 0;
    }
    .status-time {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      color: var(--ink-faint);
    }

    /* Mutants table */
    .findings-actions {
      display: flex;
      gap: 18px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .link-btn {
      appearance: none;
      background: transparent;
      border: 0;
      padding: 0;
      font: inherit;
      color: var(--ink);
      cursor: pointer;
      border-bottom: 1px solid var(--ink);
      padding-bottom: 1px;
      font-size: 0.94rem;
      font-weight: 500;
    }
    .link-btn:hover { color: var(--accent); border-bottom-color: var(--accent); }
    .link-btn[hidden] { display: none; }

    .findings-table {
      border: 1px solid var(--rule);
      border-radius: 8px;
      overflow: hidden;
    }
    .table-scroll { overflow-x: auto; }
    table.findings {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      min-width: 620px;
    }
    table.findings thead th {
      text-align: left;
      padding: 12px 16px;
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 0.78rem;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--ink-soft);
      background: var(--paper-soft);
      border-bottom: 1px solid var(--rule);
    }
    table.findings tbody td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--rule-soft);
      vertical-align: top;
    }
    table.findings tbody tr:last-child td { border-bottom: 0; }
    table.findings tbody tr:hover td { background: var(--paper-soft); }
    table.findings .id-col { width: 56px; color: var(--ink-faint); font-family: var(--font-mono); font-size: 0.84rem; }
    table.findings .line-col { width: 64px; color: var(--ink-soft); font-family: var(--font-mono); font-size: 0.88rem; }
    table.findings .status-col { width: 130px; }
    table.findings .change-col {
      min-width: 320px;
      white-space: nowrap;
    }
    table.findings .change-col code {
      display: inline-block;
      white-space: nowrap;
      max-width: 100%;
    }
    table.findings code {
      font-family: var(--font-mono);
      font-size: 0.86rem;
      background: var(--paper-soft);
      padding: 2px 6px;
      border-radius: 3px;
      border: 1px solid var(--rule);
      color: var(--ink);
    }

    /* Findings section breaks out of the 880px page width to give the
       change column real breathing room without wrapping every expression. */
    #findings-section {
      width: min(1180px, calc(100vw - 40px));
      margin-left: 50%;
      transform: translateX(-50%);
    }
    @media (max-width: 960px) {
      #findings-section {
        width: auto;
        margin-left: 0;
        transform: none;
      }
    }

    .tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 9px;
      font-family: var(--font-body);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      border-radius: 999px;
    }
    .tag::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
    .tag.killed { background: var(--good-soft); color: var(--good); }
    .tag.survived { background: var(--accent-soft); color: var(--accent-strong); }
    .tag.timeout { background: var(--warn-soft); color: var(--warn); }
    .tag.error { background: var(--info-soft); color: var(--info); }

    .empty-row td {
      padding: 36px 16px;
      text-align: center;
      color: var(--ink-faint);
      font-family: var(--font-display);
      font-style: italic;
      font-size: 1rem;
    }

    /* Help */
    .help {
      margin-top: clamp(56px, 9vw, 96px);
      padding-top: 28px;
      border-top: 1px solid var(--rule);
    }
    .help summary {
      list-style: none;
      cursor: pointer;
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.4rem;
      color: var(--ink);
      letter-spacing: -0.02em;
      display: flex;
      align-items: baseline;
      gap: 12px;
    }
    .help summary::-webkit-details-marker { display: none; }
    .help summary::before {
      content: "+";
      color: var(--accent);
      font-weight: 500;
    }
    .help[open] summary::before { content: "\2013"; }

    .help-body {
      margin-top: 24px;
      max-width: var(--measure);
    }
    .help-body h3 {
      margin: 28px 0 8px;
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 1.15rem;
      color: var(--ink);
      letter-spacing: -0.015em;
    }
    .help-body h3:first-child { margin-top: 0; }
    .help-body p, .help-body li { color: var(--ink-soft); }
    .help-body strong { color: var(--ink); font-weight: 600; }
    .help-body ol, .help-body ul { padding-left: 22px; }
    .help-body ol li, .help-body ul li { margin: 6px 0; }
    .help-body pre {
      font-family: var(--font-mono);
      font-size: 0.84rem;
      background: var(--ink);
      color: var(--paper);
      padding: 16px 18px;
      border-radius: 6px;
      overflow-x: auto;
      line-height: 1.6;
      margin: 12px 0;
    }
    .help-body code:not(pre code) {
      font-family: var(--font-mono);
      font-size: 0.88em;
      background: var(--paper-soft);
      padding: 1px 6px;
      border: 1px solid var(--rule);
      border-radius: 3px;
    }
    .legend {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px 24px;
      margin: 12px 0 4px;
    }
    .legend > div { display: flex; gap: 10px; align-items: flex-start; }
    .legend .swatch {
      width: 12px; height: 12px;
      flex-shrink: 0;
      margin-top: 6px;
      border-radius: 2px;
    }
    .legend .swatch.killed { background: var(--good); }
    .legend .swatch.survived { background: var(--accent); }
    .legend .swatch.timeout { background: var(--warn); }
    .legend .swatch.error { background: var(--info); }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(10px);
      background: var(--ink);
      color: var(--paper);
      padding: 12px 20px;
      font-family: var(--font-body);
      font-size: 0.92rem;
      font-weight: 500;
      border-radius: 6px;
      opacity: 0;
      transition: opacity 0.18s, transform 0.18s;
      pointer-events: none;
      z-index: 100;
    }
    .toast.visible { opacity: 1; transform: translateX(-50%) translateY(0); }

    /* Responsive */
    @media (max-width: 720px) {
      section.step { grid-template-columns: 1fr; gap: 8px; }
      .step-marker { font-size: 2.4rem; }
      .mode-row { grid-template-columns: 1fr; }
      .result-grid { grid-template-columns: 1fr; }
      .advanced-content { grid-template-columns: 1fr; }
      .legend { grid-template-columns: 1fr; }
    }

    @media (prefers-reduced-motion: reduce) {
      .status-dot.running { animation: none !important; }
    }
  </style>
</head>
<body>
  <main class="page">

    <!-- Top bar -->
    <header class="top">
      <span class="brand"><span class="mark"></span>Mutation Lab</span>
      <div class="lang" role="tablist" aria-label="Dil / Language">
        <button id="lang-tr-button" class="active" type="button">Türkçe</button>
        <button id="lang-en-button" type="button">English</button>
      </div>
    </header>

    <!-- Title block -->
    <h1 class="title" id="title">Testlerin <em>gerçekten</em> ne kadar güçlü?</h1>
    <p class="lede" id="lede">Mutation testing, kodda küçük değişiklikler yaparak testlerinizin bunları yakalayıp yakalamadığını ölçer.</p>
    <p class="intro-body" id="intro-body">Yakalanan değişiklik = sağlam test. Yakalanmayan değişiklik = test setinizin gözden kaçırdığı bir senaryo. Aşağıdaki üç adımı izleyerek ilk analizinizi çalıştırabilirsiniz.</p>

    <!-- 1. PROJE -->
    <section class="step" id="step1">
      <span class="step-marker">1</span>
      <div class="step-body">
        <h2 class="step-title" id="step1-title">Hangi projeyi analiz edelim?</h2>
        <p class="step-desc" id="step1-desc">Hızlıca tanışmak için hazır bir demo seçebilir, ya da kendi Python projenizi kullanabilirsiniz. Demo seçeneği önerilen başlangıçtır.</p>

        <div class="step-controls">
          <div class="mode-row">
            <label class="mode active" for="mode-demo-input">
              <input type="radio" name="mode" value="demo" id="mode-demo-input" checked>
              <div class="mode-top">
                <span class="mode-name" id="mode-demo-name">Hazır bir demo</span>
                <span class="mode-marker"></span>
              </div>
              <p class="mode-desc" id="mode-demo-desc">Üç farklı senaryodan birini seç ve tek tıkla çalıştır.</p>
            </label>
            <label class="mode" for="mode-custom-input">
              <input type="radio" name="mode" value="custom" id="mode-custom-input">
              <div class="mode-top">
                <span class="mode-name" id="mode-custom-name">Kendi projem</span>
                <span class="mode-marker"></span>
              </div>
              <p class="mode-desc" id="mode-custom-desc">Kendi Python kodunda analiz çalıştır. <code class="inline-code">pytest</code> testlerinin geçiyor olması gerekir.</p>
            </label>
          </div>

          <div class="panel" id="demo-panel">
            <div class="field">
              <label class="field-label" for="demo-select" id="demo-label">Demo seçimi</label>
              <select id="demo-select" aria-label="Choose a demo">
                <option value="beginner">Başlangıç Demosu</option>
              </select>
              <p class="field-hint" id="demo-summary">Yükleniyor…</p>
            </div>
          </div>

          <div class="panel hidden" id="custom-panel">
            <div class="field">
              <label class="field-label" for="project-root" id="project-label">Proje klasörü</label>
              <input type="text" id="project-root" value=".">
              <p class="field-hint" id="project-hint">Genelde <code class="inline-code">.</code> yeterlidir — komut zaten projenin içindeyse.</p>
            </div>
            <div class="field">
              <label class="field-label" for="source-paths" id="sources-label">Kaynak klasörler</label>
              <input type="text" id="source-paths" placeholder="src">
              <p class="field-hint" id="sources-hint">Virgülle ayrılır. Örnek: <code class="inline-code">src</code> veya <code class="inline-code">src, lib</code>.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. SAYI -->
    <section class="step" id="step2">
      <span class="step-marker">2</span>
      <div class="step-body">
        <h2 class="step-title" id="step2-title">Kaç mutasyon denesin?</h2>
        <p class="step-desc" id="step2-desc">Her mutasyon, kodda küçük bir değişiklik yapar (örneğin <code class="inline-code">&gt;</code> yerine <code class="inline-code">&gt;=</code>). Daha fazla mutasyon, daha kapsamlı analiz; ama daha uzun süre. İlk denemede <strong>10</strong> civarı dengeli bir başlangıçtır.</p>

        <div class="step-controls">
          <div class="counter-wrap">
            <div class="counter">
              <button type="button" id="count-minus" aria-label="Azalt">−</button>
              <input type="number" id="max-mutants" value="10" min="1" max="500">
              <button type="button" id="count-plus" aria-label="Artır">+</button>
            </div>
            <span class="counter-aside" id="counter-aside">mutasyon · önerilen aralık 5 – 20</span>
          </div>

          <details class="advanced">
            <summary id="advanced-summary">Gelişmiş ayarlar</summary>
            <div class="advanced-content">
              <div class="field">
                <label class="field-label" for="config-path" id="config-label">Config dosyası</label>
                <input type="text" id="config-path" placeholder="otomatik">
                <p class="field-hint" id="config-hint">Boş bırakırsanız <code class="inline-code">pyproject.toml</code> otomatik kullanılır.</p>
              </div>
              <div class="field">
                <label class="field-label" for="timeout" id="timeout-label">Zaman aşımı (saniye)</label>
                <input type="number" id="timeout" step="0.1" min="0.1" placeholder="otomatik">
                <p class="field-hint" id="timeout-hint">Boş bırakırsanız baseline süresine göre hesaplanır.</p>
              </div>
              <div class="field field-wide">
                <label class="field-label" for="operators" id="operators-label">Operatörler (opsiyonel)</label>
                <select id="operators" multiple></select>
                <p class="field-hint" id="operators-hint">Hiçbiri seçilmezse tüm varsayılan operatörler kullanılır.</p>
              </div>
              <label class="toggle" for="stop-on-survivor">
                <input type="checkbox" id="stop-on-survivor">
                <span class="toggle-text">
                  <span class="toggle-label" id="stop-label">İlk yakalanmayanda dur</span>
                  <span class="toggle-hint" id="stop-hint">Hızlı geri bildirim almak için.</span>
                </span>
              </label>
              <label class="toggle" for="fail-on-survivor">
                <input type="checkbox" id="fail-on-survivor">
                <span class="toggle-text">
                  <span class="toggle-label" id="fail-label">Yakalanmayan varsa başarısız say</span>
                  <span class="toggle-hint" id="fail-hint">CI / kalite kapısı senaryoları için.</span>
                </span>
              </label>
            </div>
          </details>

          <div class="run-row">
            <button type="button" class="run-btn" id="run-button">
              <span id="run-button-text">Analizi başlat</span>
              <span class="arrow">→</span>
            </button>
            <span class="run-hint" id="run-hint">İlk koşu birkaç saniye ile bir dakika arasında sürebilir.</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. SONUÇ -->
    <section class="step" id="step3">
      <span class="step-marker">3</span>
      <div class="step-body">
        <h2 class="step-title" id="step3-title">Sonuçlar</h2>
        <p class="step-desc" id="step3-desc">Mutasyon skoru, kaç değişikliğin testleriniz tarafından yakalandığını gösterir. Yüksek skor güçlü test seti, düşük skor ise eksik test senaryoları anlamına gelir.</p>

        <div class="result-grid">
          <div class="score-stack">
            <p class="score-label" id="score-label">Mutasyon Skoru</p>
            <div class="score-value"><span id="score-value">—</span><span class="unit" id="score-unit">%</span></div>
            <p class="score-narrate" id="score-narrate">Henüz çalıştırılmadı. Yukarıdaki <strong>Analizi başlat</strong> düğmesine bas.</p>
          </div>

          <div class="breakdown">
            <div class="bd-row good">
              <span class="bd-glyph">✓</span>
              <span class="bd-name" id="killed-label">Yakalanan<span class="bd-detail" id="killed-detail">Test fail oldu — değişiklik tespit edildi.</span></span>
              <span class="bd-value" id="killed-value">0</span>
            </div>
            <div class="bd-row bad">
              <span class="bd-glyph">●</span>
              <span class="bd-name" id="survived-label">Yakalanmayan<span class="bd-detail" id="survived-detail">Test geçti — değişiklik gözden kaçtı.</span></span>
              <span class="bd-value" id="survived-value">0</span>
            </div>
            <div class="bd-row warn">
              <span class="bd-glyph">⧗</span>
              <span class="bd-name" id="timeout-label">Zaman aşımı<span class="bd-detail" id="timeout-detail">Mutasyon çok yavaşladı.</span></span>
              <span class="bd-value" id="timeout-value">0</span>
            </div>
            <div class="bd-row info">
              <span class="bd-glyph">✗</span>
              <span class="bd-name" id="error-label">Hata<span class="bd-detail" id="error-detail">Mutasyon syntax/import hatası üretti.</span></span>
              <span class="bd-value" id="error-value">0</span>
            </div>
          </div>
        </div>

        <div class="status-strip">
          <span class="status-dot" id="status-dot"></span>
          <span class="status-label" id="status-label">Hazır</span>
          <span class="status-msg" id="status-message">Başlamaya hazır.</span>
          <span class="status-time" id="status-time"></span>
        </div>
      </div>
    </section>

    <!-- 4. BULGULAR -->
    <section class="step" id="findings-section" hidden>
      <span class="step-marker">4</span>
      <div class="step-body">
        <h2 class="step-title" id="step4-title">Bulgular</h2>
        <p class="step-desc" id="step4-desc">Aşağıdaki mutasyonlar test setinizden kaçanlardır. Her satır, eksik bir test senaryosunun ipucudur — bu değişikliği yakalayan bir test eklerseniz, skor yükselir.</p>

        <div class="findings-actions">
          <button type="button" class="link-btn" id="download-report-button" hidden>↓ Download Latest Report</button>
          <button type="button" class="link-btn" id="download-pdf-button" hidden>↓ Download Latest PDF</button>
        </div>

        <div class="findings-table">
          <div class="table-scroll">
            <table class="findings">
              <thead>
                <tr>
                  <th class="id-col">#</th>
                  <th id="th-file">Dosya</th>
                  <th class="line-col" id="th-line">Satır</th>
                  <th class="status-col" id="th-status">Durum</th>
                  <th id="th-change">Değişiklik</th>
                </tr>
              </thead>
              <tbody id="mutant-body">
                <tr class="empty-row"><td colspan="5" id="empty-mutants">Henüz mutasyon çalıştırılmadı.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- HELP -->
    <details class="help">
      <summary id="help-summary">How To Use Mutation Lab</summary>
      <div class="help-body" id="help-body-tr">
        <h3>Mutation testing nedir?</h3>
        <p>Kodunuza kasıtlı olarak küçük değişiklikler (mutasyonlar) yapılır ve testlerinizin bu değişiklikleri yakalayıp yakalamadığı ölçülür. Test fail olursa <strong>mutant yakalandı</strong> — testleriniz sağlam. Test hâlâ geçerse <strong>mutant yakalanmadı</strong> — testlerinizde eksik bir senaryo var demektir.</p>

        <h3>Adım adım</h3>
        <ol>
          <li>Bir <strong>demo</strong> seçin ya da <strong>kendi projenizi</strong> kullanın.</li>
          <li>Bir <strong>mutasyon sayısı</strong> belirleyin (5–20 arası bir başlangıç için iyidir).</li>
          <li><strong>Analizi başlat</strong> düğmesine basın.</li>
          <li>Sonuç skorunu okuyun. Yakalanmayan mutasyonlar varsa, her birini inceleyin ve eksik test senaryolarını yazın.</li>
        </ol>

        <h3>Durum açıklamaları</h3>
        <div class="legend">
          <div><span class="swatch killed"></span><div><strong>Yakalanan</strong> — testler bu değişikliği fark etti.</div></div>
          <div><span class="swatch survived"></span><div><strong>Yakalanmayan</strong> — testler bu değişikliği fark etmedi. Eksik senaryo.</div></div>
          <div><span class="swatch timeout"></span><div><strong>Zaman aşımı</strong> — mutasyon çok yavaşladı. Sonsuz döngü olabilir.</div></div>
          <div><span class="swatch error"></span><div><strong>Hata</strong> — mutasyon syntax veya import hatasına yol açtı.</div></div>
        </div>

        <h3>Önerilen <code>pyproject.toml</code></h3>
        <pre>[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**"]</pre>

        <h3>Komut satırı eşdeğerleri</h3>
        <pre>python -m mutation_tool run . --max-mutants 10
python -m mutation_tool list-operators
python -m mutation_tool ui</pre>
      </div>

      <div class="help-body" id="help-body-en" hidden>
        <h3>What is mutation testing?</h3>
        <p>The tool makes small intentional changes (mutants) to your code and checks whether your tests catch them. If a test fails afterward, the <strong>mutant was caught</strong> — your tests are solid. If tests still pass, the <strong>mutant survived</strong> — your tests have a missing scenario.</p>

        <h3>Step by step</h3>
        <ol>
          <li>Pick a <strong>demo</strong> or use <strong>your own project</strong>.</li>
          <li>Choose a <strong>mutant count</strong> (5–20 is a good starting range).</li>
          <li>Press <strong>Start analysis</strong>.</li>
          <li>Read the score. For each survivor, inspect the change and write the missing test.</li>
        </ol>

        <h3>Status legend</h3>
        <div class="legend">
          <div><span class="swatch killed"></span><div><strong>Caught</strong> — tests noticed the change.</div></div>
          <div><span class="swatch survived"></span><div><strong>Survived</strong> — tests missed the change. Missing scenario.</div></div>
          <div><span class="swatch timeout"></span><div><strong>Timeout</strong> — mutant got slow. Possible infinite loop.</div></div>
          <div><span class="swatch error"></span><div><strong>Error</strong> — mutant caused a syntax or import error.</div></div>
        </div>

        <h3>Recommended <code>pyproject.toml</code></h3>
        <pre>[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**"]</pre>

        <h3>Command-line equivalents</h3>
        <pre>python -m mutation_tool run . --max-mutants 10
python -m mutation_tool list-operators
python -m mutation_tool ui</pre>
      </div>
    </details>
  </main>

  <div class="toast" id="toast"></div>

  <script>
    const LANG_KEY = 'mutation-lab-language';

    const I18N = {
      tr: {
        langTr: 'Türkçe', langEn: 'English',
        titleHtml: 'Testlerin <em>gerçekten</em> ne kadar güçlü?',
        lede: 'Mutation testing, kodda küçük değişiklikler yaparak testlerinizin bunları yakalayıp yakalamadığını ölçer.',
        introBody: 'Yakalanan değişiklik = sağlam test. Yakalanmayan değişiklik = test setinizin gözden kaçırdığı bir senaryo. Aşağıdaki üç adımı izleyerek ilk analizinizi çalıştırabilirsiniz.',
        step1: 'Hangi projeyi analiz edelim?',
        step1Desc: 'Hızlıca tanışmak için hazır bir demo seçebilir, ya da kendi Python projenizi kullanabilirsiniz. Demo seçeneği önerilen başlangıçtır.',
        modeDemoName: 'Hazır bir demo',
        modeDemoDesc: 'Üç farklı senaryodan birini seç ve tek tıkla çalıştır.',
        modeCustomName: 'Kendi projem',
        modeCustomDescHtml: 'Kendi Python kodunda analiz çalıştır. <code class="inline-code">pytest</code> testlerinin geçiyor olması gerekir.',
        demoLabel: 'Demo seçimi',
        projectLabel: 'Proje klasörü',
        projectHintHtml: 'Genelde <code class="inline-code">.</code> yeterlidir — komut zaten projenin içindeyse.',
        sourcesLabel: 'Kaynak klasörler',
        sourcesHintHtml: 'Virgülle ayrılır. Örnek: <code class="inline-code">src</code> veya <code class="inline-code">src, lib</code>.',
        step2: 'Kaç mutasyon denesin?',
        step2DescHtml: 'Her mutasyon, kodda küçük bir değişiklik yapar (örneğin <code class="inline-code">&gt;</code> yerine <code class="inline-code">&gt;=</code>). Daha fazla mutasyon, daha kapsamlı analiz; ama daha uzun süre. İlk denemede <strong>10</strong> civarı dengeli bir başlangıçtır.',
        counterAside: 'mutasyon · önerilen aralık 5 – 20',
        advancedSummary: 'Gelişmiş ayarlar',
        configLabel: 'Config dosyası',
        configHintHtml: 'Boş bırakırsanız <code class="inline-code">pyproject.toml</code> otomatik kullanılır.',
        timeoutLabel: 'Zaman aşımı (saniye)',
        timeoutHint: 'Boş bırakırsanız baseline süresine göre hesaplanır.',
        operatorsLabel: 'Operatörler (opsiyonel)',
        operatorsHint: 'Hiçbiri seçilmezse tüm varsayılan operatörler kullanılır.',
        stopLabel: 'İlk yakalanmayanda dur',
        stopHint: 'Hızlı geri bildirim almak için.',
        failLabel: 'Yakalanmayan varsa başarısız say',
        failHint: 'CI / kalite kapısı senaryoları için.',
        runText: 'Analizi başlat',
        runRunning: 'Çalışıyor…',
        runHint: 'İlk koşu birkaç saniye ile bir dakika arasında sürebilir.',
        step3: 'Sonuçlar',
        step3Desc: 'Mutasyon skoru, kaç değişikliğin testleriniz tarafından yakalandığını gösterir. Yüksek skor güçlü test seti, düşük skor ise eksik test senaryoları anlamına gelir.',
        scoreLabel: 'Mutasyon Skoru',
        killedLabel: 'Yakalanan',
        killedDetail: 'Test fail oldu — değişiklik tespit edildi.',
        survivedLabel: 'Yakalanmayan',
        survivedDetail: 'Test geçti — değişiklik gözden kaçtı.',
        timeoutLabel2: 'Zaman aşımı',
        timeoutDetail: 'Mutasyon çok yavaşladı.',
        errorLabel: 'Hata',
        errorDetail: 'Mutasyon syntax/import hatası üretti.',
        statusIdle: 'Hazır',
        statusRunning: 'Çalışıyor',
        statusCompleted: 'Tamamlandı',
        statusFailed: 'Hata',
        msgReady: 'Başlamaya hazır.',
        msgRunning: 'Mutasyon analizi çalışıyor — birkaç dakika sürebilir.',
        msgCompleted: 'Analiz tamamlandı.',
        msgFailed: 'Analiz başarısız oldu.',
        narrateIdleHtml: 'Henüz çalıştırılmadı. Yukarıdaki <strong>Analizi başlat</strong> düğmesine bas.',
        narrateRunningHtml: 'Mutasyonlar üretildi, baseline alındı. Test paketin koşturuluyor…',
        narrateSurvivorsHtml: (n) => `Test setiniz <strong>${n} mutasyonu</strong> yakalayamadı. Aşağıdaki tabloyu inceleyerek eksik test senaryolarını bulabilirsiniz.`,
        narrateCleanHtml: 'Tüm mutasyonlar testleriniz tarafından yakalandı. Bu örneklem için test setiniz <strong>sağlam</strong>.',
        narrateNoMutantsHtml: 'Hiç mutasyon çalıştırılmadı. Kapsamı veya operatör seçimini kontrol et.',
        narrateFailedHtml: 'Analiz başarısız. Aşağıdaki durum satırında detayları görebilirsin.',
        step4: 'Bulgular',
        step4Desc: 'Aşağıdaki mutasyonlar test setinizden kaçanlardır. Her satır, eksik bir test senaryosunun ipucudur — bu değişikliği yakalayan bir test eklerseniz, skor yükselir.',
        thFile: 'Dosya',
        thLine: 'Satır',
        thStatus: 'Durum',
        thChange: 'Değişiklik',
        emptyMutants: 'Henüz mutasyon çalıştırılmadı.',
        emptyMutantsRun: 'Bu koşuda hiç mutasyon çalıştırılmadı.',
        downloadJson: '↓ Download Latest Report',
        downloadPdf: '↓ Download Latest PDF',
        toastDownloadEmpty: 'Henüz indirilebilecek bir rapor yok.',
        helpSummary: 'How To Use Mutation Lab',
        tagKilled: 'Yakalandı',
        tagSurvived: 'Kaçtı',
        tagTimeout: 'Timeout',
        tagError: 'Hata',
      },
      en: {
        langTr: 'Türkçe', langEn: 'English',
        titleHtml: 'How <em>strong</em> are your tests, really?',
        lede: 'Mutation testing makes tiny changes in your code and measures whether your tests catch them.',
        introBody: 'A caught change means a solid test. A missed change is a scenario your test suite forgot. Follow the three steps below to run your first analysis.',
        step1: 'Which project should we analyze?',
        step1Desc: 'You can pick a ready-made demo for a quick tour, or use your own Python project. Starting with a demo is the recommended path.',
        modeDemoName: 'A built-in demo',
        modeDemoDesc: 'Pick from three scenarios and run with a single click.',
        modeCustomName: 'My own project',
        modeCustomDescHtml: 'Run analysis on your own Python code. Your <code class="inline-code">pytest</code> suite must already pass.',
        demoLabel: 'Choose a demo',
        projectLabel: 'Project folder',
        projectHintHtml: 'Usually <code class="inline-code">.</code> is enough — when the terminal is inside the project.',
        sourcesLabel: 'Source folders',
        sourcesHintHtml: 'Comma-separated. e.g. <code class="inline-code">src</code> or <code class="inline-code">src, lib</code>.',
        step2: 'How many mutations should we try?',
        step2DescHtml: 'Each mutation makes a small change in your code (for example <code class="inline-code">&gt;</code> becomes <code class="inline-code">&gt;=</code>). More mutations means broader analysis, but takes longer. For a first try, <strong>10</strong> is a balanced starting point.',
        counterAside: 'mutations · recommended range 5 – 20',
        advancedSummary: 'Advanced settings',
        configLabel: 'Config file',
        configHintHtml: 'Leave empty to use <code class="inline-code">pyproject.toml</code> automatically.',
        timeoutLabel: 'Timeout (seconds)',
        timeoutHint: 'Leave empty to compute from baseline duration.',
        operatorsLabel: 'Operators (optional)',
        operatorsHint: 'If none are selected, all default operators are used.',
        stopLabel: 'Stop on first survivor',
        stopHint: 'For fast local feedback.',
        failLabel: 'Fail if a survivor exists',
        failHint: 'For CI / quality-gate scenarios.',
        runText: 'Start analysis',
        runRunning: 'Running…',
        runHint: 'The first run can take a few seconds to a minute.',
        step3: 'Results',
        step3Desc: 'The mutation score shows how many changes your tests caught. A high score means a strong test suite; a low score points to missing test scenarios.',
        scoreLabel: 'Mutation score',
        killedLabel: 'Caught',
        killedDetail: 'A test failed — the change was detected.',
        survivedLabel: 'Survived',
        survivedDetail: 'Tests still passed — the change was missed.',
        timeoutLabel2: 'Timeout',
        timeoutDetail: 'The mutant ran too slowly.',
        errorLabel: 'Error',
        errorDetail: 'The mutant produced a syntax or import error.',
        statusIdle: 'Idle',
        statusRunning: 'Running',
        statusCompleted: 'Completed',
        statusFailed: 'Failed',
        msgReady: 'Ready to start.',
        msgRunning: 'Mutation analysis is running — may take a few minutes.',
        msgCompleted: 'Analysis completed.',
        msgFailed: 'Analysis failed.',
        narrateIdleHtml: 'Not run yet. Press <strong>Start analysis</strong> above to begin.',
        narrateRunningHtml: 'Mutants generated, baseline captured. Running your test suite…',
        narrateSurvivorsHtml: (n) => `Your tests missed <strong>${n} mutations</strong>. Inspect the table below to find the missing scenarios.`,
        narrateCleanHtml: 'All mutations were caught by your tests. The suite is <strong>solid</strong> for this sample.',
        narrateNoMutantsHtml: 'No mutations were executed. Check the scope or operator selection.',
        narrateFailedHtml: 'Analysis failed. See the status line below for details.',
        step4: 'Findings',
        step4Desc: 'The mutations below escaped your test suite. Each one is a hint for a missing test scenario — add a test that catches the change, and your score will go up.',
        thFile: 'File',
        thLine: 'Line',
        thStatus: 'Status',
        thChange: 'Change',
        emptyMutants: 'No mutations run yet.',
        emptyMutantsRun: 'This run executed no mutations.',
        downloadJson: '↓ Download Latest Report',
        downloadPdf: '↓ Download Latest PDF',
        toastDownloadEmpty: 'No report available yet.',
        helpSummary: 'How To Use Mutation Lab',
        tagKilled: 'Caught',
        tagSurvived: 'Survived',
        tagTimeout: 'Timeout',
        tagError: 'Error',
      },
    };

    let currentLang = 'en';
    let demoCatalog = [];
    let lastSnapshot = null;
    let pollingStarted = false;

    const $ = (id) => document.getElementById(id);
    const T = () => I18N[currentLang];

    function escapeHtml(value) {
      return String(value == null ? '' : value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }
    function pad(n, w) { return String(n).padStart(w, '0'); }

    function showToast(message) {
      const t = $('toast');
      t.textContent = message;
      t.classList.add('visible');
      setTimeout(() => t.classList.remove('visible'), 2400);
    }

    function setLang(lang) {
      currentLang = lang === 'en' ? 'en' : 'tr';
      try { localStorage.setItem(LANG_KEY, currentLang); } catch (e) {}
      document.documentElement.lang = currentLang;
      $('lang-tr-button').classList.toggle('active', currentLang === 'tr');
      $('lang-en-button').classList.toggle('active', currentLang === 'en');

      const L = T();
      $('lang-tr-button').textContent = L.langTr;
      $('lang-en-button').textContent = L.langEn;
      $('title').innerHTML = L.titleHtml;
      $('lede').textContent = L.lede;
      $('intro-body').textContent = L.introBody;

      $('step1-title').textContent = L.step1;
      $('step1-desc').textContent = L.step1Desc;
      $('mode-demo-name').textContent = L.modeDemoName;
      $('mode-demo-desc').textContent = L.modeDemoDesc;
      $('mode-custom-name').textContent = L.modeCustomName;
      $('mode-custom-desc').innerHTML = L.modeCustomDescHtml;
      $('demo-label').textContent = L.demoLabel;
      $('project-label').textContent = L.projectLabel;
      $('project-hint').innerHTML = L.projectHintHtml;
      $('sources-label').textContent = L.sourcesLabel;
      $('sources-hint').innerHTML = L.sourcesHintHtml;

      $('step2-title').textContent = L.step2;
      $('step2-desc').innerHTML = L.step2DescHtml;
      $('counter-aside').textContent = L.counterAside;
      $('advanced-summary').textContent = L.advancedSummary;
      $('config-label').textContent = L.configLabel;
      $('config-hint').innerHTML = L.configHintHtml;
      $('timeout-label').textContent = L.timeoutLabel;
      $('timeout-hint').textContent = L.timeoutHint;
      $('operators-label').textContent = L.operatorsLabel;
      $('operators-hint').textContent = L.operatorsHint;
      $('stop-label').textContent = L.stopLabel;
      $('stop-hint').textContent = L.stopHint;
      $('fail-label').textContent = L.failLabel;
      $('fail-hint').textContent = L.failHint;
      $('run-button-text').textContent = (lastSnapshot.status === 'running') ? L.runRunning : L.runText;
      $('run-hint').textContent = L.runHint;

      $('step3-title').textContent = L.step3;
      $('step3-desc').textContent = L.step3Desc;
      $('score-label').textContent = L.scoreLabel;
      $('killed-label').firstChild.textContent = L.killedLabel;
      $('killed-detail').textContent = L.killedDetail;
      $('survived-label').firstChild.textContent = L.survivedLabel;
      $('survived-detail').textContent = L.survivedDetail;
      $('timeout-label').textContent = L.timeoutLabel;
      // timeout uses a separate label inside bd-name
      $('timeout-detail').textContent = L.timeoutDetail;
      $('error-label').firstChild.textContent = L.errorLabel;
      $('error-detail').textContent = L.errorDetail;

      $('step4-title').textContent = L.step4;
      $('step4-desc').textContent = L.step4Desc;
      $('th-file').textContent = L.thFile;
      $('th-line').textContent = L.thLine;
      $('th-status').textContent = L.thStatus;
      $('th-change').textContent = L.thChange;
      $('empty-mutants').textContent = L.emptyMutants;
      $('download-report-button').textContent = L.downloadJson;
      $('download-pdf-button').textContent = L.downloadPdf;
      $('help-summary').textContent = L.helpSummary;

      Array.from($('demo-select').options).forEach((opt) => {
        const label = opt.dataset[currentLang];
        if (label) opt.textContent = label;
      });
      $('help-body-tr').hidden = currentLang !== 'tr';
      $('help-body-en').hidden = currentLang !== 'en';

      // Fix bd-name labels (they have a child detail span)
      fixBdName('killed-label', L.killedLabel);
      fixBdName('survived-label', L.survivedLabel);
      fixBdName('timeout-bd-label', L.timeoutLabel2);
      fixBdName('error-label', L.errorLabel);

      updateDemoSummary();
      renderStatus(lastSnapshot);
    }

    function fixBdName(id, text) {
      const el = $(id);
      if (!el) return;
      const detail = el.querySelector('.bd-detail');
      el.firstChild.textContent = text;
      if (detail) el.appendChild(detail);
    }

    function activeMode() {
      const checked = document.querySelector('input[name=mode]:checked');
      return checked ? checked.value : 'demo';
    }

    function applyMode() {
      const mode = activeMode();
      document.querySelectorAll('.mode').forEach((m) => {
        const input = m.querySelector('input[type=radio]');
        m.classList.toggle('active', input && input.value === mode);
      });
      $('demo-panel').classList.toggle('hidden', mode !== 'demo');
      $('custom-panel').classList.toggle('hidden', mode !== 'custom');
    }

    function updateDemoSummary() {
      const id = $('demo-select').value;
      const demo = demoCatalog.find((d) => d.id === id);
      if (!demo) return;
      const summary = (demo.summary && demo.summary[currentLang]) || (demo.summary && demo.summary.en) || '';
      $('demo-summary').textContent = summary;
    }

    async function loadDemoCatalog() {
      try {
        const res = await fetch('/api/demos');
        const data = await res.json();
        demoCatalog = data.demos || [];
        populateDemoDropdown();
        updateDemoSummary();
      } catch (e) {}
    }

    function populateDemoDropdown() {
      const select = $('demo-select');
      const previousValue = select.value;
      select.innerHTML = '';
      demoCatalog.forEach((d) => {
        const opt = document.createElement('option');
        opt.value = d.id;
        opt.textContent = (d.name && d.name[currentLang]) || d.id;
        select.appendChild(opt);
      });
      if (demoCatalog.some((d) => d.id === previousValue)) {
        select.value = previousValue;
      }
    }

    async function loadOperators() {
      try {
        const res = await fetch('/api/operators');
        const data = await res.json();
        const sel = $('operators');
        sel.innerHTML = '';
        (data.operators || []).forEach((name) => {
          const o = document.createElement('option');
          o.value = name;
          o.textContent = name;
          sel.appendChild(o);
        });
      } catch (e) {}
    }

    function setCount(value) {
      const n = Math.max(1, Math.min(500, Math.round(Number(value) || 10)));
      $('max-mutants').value = n;
      return n;
    }

    function readAdvancedOverrides() {
      const max = $('max-mutants').value ? Number($('max-mutants').value) : null;
      const timeout = $('timeout').value ? Number($('timeout').value) : null;
      const ops = Array.from($('operators').selectedOptions).map((o) => o.value);
      const stopOn = $('stop-on-survivor').checked;
      const failOn = $('fail-on-survivor').checked;
      const cfg = $('config-path').value.trim() || null;
      return { max, timeout, ops, stopOn, failOn, cfg };
    }

    async function fetchDemoPreset(demoId) {
      const res = await fetch('/api/demo-preset?demo_id=' + encodeURIComponent(demoId));
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.detail || 'Demo could not be loaded.');
      }
      return res.json();
    }

    async function startRun() {
      const mode = activeMode();
      const adv = readAdvancedOverrides();
      let body;

      if (mode === 'demo') {
        try {
          const preset = await fetchDemoPreset($('demo-select').value);
          body = Object.assign({}, preset.request);
          if (adv.max) body.max_mutants = adv.max;
          if (adv.timeout) body.per_mutant_timeout = adv.timeout;
          if (adv.ops.length) body.operators = adv.ops;
          if (adv.stopOn) body.stop_on_survivor = true;
          if (adv.failOn) body.fail_on_survivor = true;
          if (adv.cfg) body.config_path = adv.cfg;
        } catch (e) {
          renderStatus({ status: 'failed', message: e.message, error: e.message });
          return;
        }
      } else {
        const root = $('project-root').value.trim() || '.';
        const sources = $('source-paths').value.split(',').map((s) => s.trim()).filter(Boolean);
        body = {
          project_root: root,
          source_paths: sources,
          max_mutants: adv.max,
          per_mutant_timeout: adv.timeout,
          operators: adv.ops,
          stop_on_survivor: adv.stopOn,
          fail_on_survivor: adv.failOn,
          config_path: adv.cfg,
        };
      }

      $('run-button').disabled = true;
      $('run-button-text').textContent = T().runRunning;

      try {
        const res = await fetch('/api/run', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });
        const data = await res.json();
        if (!res.ok) {
          renderStatus({ status: 'failed', message: data.detail || 'Failed', error: data.detail || 'Failed' });
        } else {
          renderStatus(data);
        }
      } catch (e) {
        renderStatus({ status: 'failed', message: e.message, error: e.message });
      }
    }

    function statusLabel(status) {
      const L = T();
      switch (status) {
        case 'running': return L.statusRunning;
        case 'completed': return L.statusCompleted;
        case 'failed': return L.statusFailed;
        default: return L.statusIdle;
      }
    }

    function translateBackendMessage(msg) {
      if (!msg) return T().msgReady;
      const map = {
        'Ready to launch mutation analysis.': 'msgReady',
        'Mutation analysis is running.': 'msgRunning',
        'Mutation analysis completed.': 'msgCompleted',
        'Mutation analysis failed.': 'msgFailed',
      };
      if (map[msg]) return T()[map[msg]];
      return msg;
    }

    function fmtClock(d) {
      return pad(d.getHours(), 2) + ':' + pad(d.getMinutes(), 2) + ':' + pad(d.getSeconds(), 2);
    }
    function formatTimeRange(snapshot) {
      const start = snapshot.started_at ? new Date(snapshot.started_at) : null;
      const end = snapshot.finished_at ? new Date(snapshot.finished_at) : null;
      if (start && end) return fmtClock(start) + ' → ' + fmtClock(end);
      if (start) return fmtClock(start) + ' …';
      return '';
    }

    function narrateScore(snapshot, status) {
      const L = T();
      if (status === 'idle') return L.narrateIdleHtml;
      if (status === 'running') return L.narrateRunningHtml;
      if (status === 'failed') return L.narrateFailedHtml;
      const summary = snapshot.result && snapshot.result.summary;
      if (!summary) return L.narrateIdleHtml;
      if (!summary.executed) return L.narrateNoMutantsHtml;
      if ((summary.survived || 0) > 0) return L.narrateSurvivorsHtml(summary.survived);
      return L.narrateCleanHtml;
    }

    function renderStatus(snapshot) {
      if (!snapshot) snapshot = { status: 'idle' };
      lastSnapshot = snapshot;
      const status = snapshot.status || 'idle';
      const L = T();

      $('status-dot').className = 'status-dot ' + status;
      $('status-label').textContent = statusLabel(status);
      $('status-message').textContent = translateBackendMessage(snapshot.error || snapshot.message);
      $('status-time').textContent = formatTimeRange(snapshot);

      const isRunning = status === 'running';
      $('run-button').disabled = isRunning;
      $('run-button-text').textContent = isRunning ? L.runRunning : L.runText;

      const summary = snapshot.result && snapshot.result.summary;
      if (summary) {
        $('score-value').textContent = Number(summary.mutation_score || 0).toFixed(0);
        $('score-unit').style.display = '';
        $('killed-value').textContent = String(summary.killed || 0);
        $('survived-value').textContent = String(summary.survived || 0);
        $('timeout-value').textContent = String(summary.timeout || 0);
        $('error-value').textContent = String(summary.error || 0);
      } else if (isRunning) {
        $('score-value').textContent = '…';
        $('score-unit').style.display = 'none';
      } else {
        $('score-value').textContent = '—';
        $('score-unit').style.display = 'none';
        $('killed-value').textContent = '0';
        $('survived-value').textContent = '0';
        $('timeout-value').textContent = '0';
        $('error-value').textContent = '0';
      }
      $('score-narrate').innerHTML = narrateScore(snapshot, status);

      const hasReport = !!snapshot.report_path;
      const hasPdf = !!snapshot.pdf_report_path;
      $('download-report-button').hidden = !hasReport;
      $('download-pdf-button').hidden = !hasPdf;

      const mutants = (snapshot.result && snapshot.result.mutants) || [];
      const findings = $('findings-section');
      if (mutants.length > 0 || status === 'completed' || status === 'failed' || hasReport) {
        findings.hidden = false;
        renderMutants(mutants);
      } else if (status === 'idle') {
        findings.hidden = true;
      }
    }

    function renderMutants(mutants) {
      const tbody = $('mutant-body');
      const L = T();
      if (!mutants.length) {
        tbody.innerHTML = '<tr class="empty-row"><td colspan="5">' + escapeHtml(L.emptyMutantsRun) + '</td></tr>';
        return;
      }
      const tagText = { killed: L.tagKilled, survived: L.tagSurvived, timeout: L.tagTimeout, error: L.tagError };
      tbody.innerHTML = mutants.map((m, idx) => {
        const status = String(m.status || 'unknown').toLowerCase();
        const line = (m.location && m.location.start_line) || '—';
        const original = escapeHtml(m.original_snippet || '');
        const mutated = escapeHtml(m.mutated_snippet || '');
        const label = tagText[status] || status;
        return '<tr>' +
          '<td class="id-col">' + pad(idx + 1, 3) + '</td>' +
          '<td><code>' + escapeHtml(m.file_path || '') + '</code></td>' +
          '<td class="line-col">' + escapeHtml(line) + '</td>' +
          '<td class="status-col"><span class="tag ' + status + '">' + escapeHtml(label) + '</span></td>' +
          '<td class="change-col"><code>' + original + ' → ' + mutated + '</code></td>' +
          '</tr>';
      }).join('');
    }

    async function refreshStatus() {
      try {
        const res = await fetch('/api/status');
        if (!res.ok) return;
        const data = await res.json();
        renderStatus(data);
      } catch (e) {}
    }

    function startPolling() {
      if (pollingStarted) return;
      pollingStarted = true;
      setInterval(refreshStatus, 2000);
    }

    function downloadJson() {
      if (!lastSnapshot.report_path) { showToast(T().toastDownloadEmpty); return; }
      window.location.href = '/api/report/download';
    }
    function downloadPdf() {
      if (!lastSnapshot.pdf_report_path) { showToast(T().toastDownloadEmpty); return; }
      window.location.href = '/api/report/download/pdf';
    }

    document.addEventListener('DOMContentLoaded', () => {
      // Add id markers for the timeout row label since it conflicts with the field above
      const timeoutBd = document.querySelector('.bd-row.warn .bd-name');
      if (timeoutBd) timeoutBd.id = 'timeout-bd-label';

      $('lang-tr-button').addEventListener('click', () => setLang('tr'));
      $('lang-en-button').addEventListener('click', () => setLang('en'));
      document.querySelectorAll('input[name=mode]').forEach((r) => r.addEventListener('change', applyMode));
      $('count-minus').addEventListener('click', () => setCount(Number($('max-mutants').value) - 1));
      $('count-plus').addEventListener('click', () => setCount(Number($('max-mutants').value) + 1));
      $('max-mutants').addEventListener('blur', () => setCount($('max-mutants').value));
      $('demo-select').addEventListener('change', updateDemoSummary);
      $('run-button').addEventListener('click', startRun);
      $('download-report-button').addEventListener('click', downloadJson);
      $('download-pdf-button').addEventListener('click', downloadPdf);

      setLang(currentLang);
      applyMode();
      setCount($('max-mutants').value);
      loadDemoCatalog();
      loadOperators();
      refreshStatus();
      startPolling();
    });
  </script>
</body>
</html>
"""
