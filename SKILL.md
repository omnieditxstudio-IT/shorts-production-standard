---
name: shorts-production-standard
description: 'Production standard for polished 9:16 social shorts. Use whenever creating, editing, reviewing, rendering, or exporting a YouTube Short, TikTok, Reel, or vertical clip. Applies a consistent Remotion-style visual template and QA baseline across video skills.'
---

# Shorts Production Standard

Use this alongside the task-specific video skill. It is the shared house style,
not a replacement for cutting, captioning, or rendering tools.

## Required edit standard

- Use a 1080x1920, 30 fps composition with a single active audio source.
- Default source treatment: `layout: scale`, static `scaleFactor: 2.5`, centred.
  Set `1.0` only when the user explicitly requests the entire source frame.
- Keep `zoomIntro: 1` and `zoomIntroSec: 0` unless an intro camera move is requested.
- Use brief face/reaction punch-ins only at real decision, reveal, or emotion beats.
- Add restrained white flashes at hard decisions/cuts and gold flash/pop only at a win or payoff.
- Captions: bold ALL CAPS, word-synced, yellow active word, black outline, subtle shadow,
  and positioned above platform controls. No coloured caption glow.
- Brand badge sits top-centre after the hook. Glow belongs only on centred payoff labels.

## Caption hygiene

Remove non-spoken YouTube caption markers (`>>`, `>>>`, `&gt;&gt;`) before every preview
and render. Correct obvious names and monetary amounts from context.

## Quality loop

1. Preview in Studio and confirm actual `scaleFactor` before rendering.
2. Render one master unless platform variants are specifically requested.
3. Inspect a contact sheet after picture/colour changes: hook, face beat, cut, payoff, end.
4. Verify final 1080x1920, 30 fps, H.264/AAC, duration and delivery path.

## Colour correction

For standard SDR footage, keep corrections restrained: exposure `+0.04`, contrast `1.08`,
saturation `1.07`, gamma `1.02`. Preserve an ungraded master and write a separate `_cc` file.
