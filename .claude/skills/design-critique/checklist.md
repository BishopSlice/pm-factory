# Critique checklist (load only during design-critique)

## 1. Clarity and hierarchy
- C1 The main action on each screen is obvious within 3 seconds.
- C2 There is one clear focal point per screen, not several competing ones.
- C3 Labels use the user's words, not system terms.
- C4 Related items are grouped, and unrelated ones are separated by space.
- C5 Nothing decorative competes with content.

## 2. Flow and effort
- F1 The main task takes the fewest reasonable steps.
- F2 Choices are limited at each step. Defaults are sensible.
- F3 Users never have to remember something from a previous screen.
- F4 Destructive actions need confirmation or are undoable.
- F5 Forms validate inline and explain how to fix errors.

## 3. States and feedback
- S1 Every action gives visible feedback within about 100 ms.
- S2 Loading states show progress or a skeleton, not a frozen screen.
- S3 Empty states explain what will appear and how to start.
- S4 Errors say what happened and what to do, without blame.
- S5 Success is confirmed, and the next step is clear.

## 4. AI product trust
- A1 AI output is clearly marked as AI-generated.
- A2 Claims show their sources, and sources open in one click.
- A3 Users can stop, edit or regenerate AI output.
- A4 Uncertainty is shown ("I'm not sure") instead of being hidden.
- A5 Actions on the user's behalf need approval if the spec says Ask first.
- A6 Failures fall back gracefully with a retry option.

## 5. Technical quality
- T1 Text contrast is at least 4.5:1 (3:1 for large text) in both themes.
- T2 Everything works by keyboard, and focus is always visible.
- T3 Images and icons have text alternatives. Form fields have labels.
- T4 Layout works at 375 px wide with no sideways scroll.
- T5 Touch targets are at least 44 px.
- T6 There are no console errors on the main path.
- T7 Motion respects the reduced-motion setting.
