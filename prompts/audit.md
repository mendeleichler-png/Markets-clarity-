# Stage prompt — Build audit
Audit the built MP4 against config/gates.yaml. Run src/qa_gates.py for the measured
gates; pull one frame per shot for the framing audit; run three hostile critique
cycles (dead spots, weak/irrelevant shots, caption drift, repeated clips, audio
issues), fixing and re-rendering between cycles. Write audit.md: every gate with its
measured value and PASS/FAIL, the framing frames, the three critique lists, and a
"vs the floor" line naming the one craft dimension this build pushes past anything
the channel has shipped.
