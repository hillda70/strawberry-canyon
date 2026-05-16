\# Cross-Asset Session Force Surface



This is the first canonical Strawberry Canyon sample surface.



It transforms cross-asset market data into a normalized state-detection layer.



\---



\# Fields



| Field | Meaning |

|---|---|

| Session\_F | Current session directional force |

| Session\_F\_PRV | Prior session directional force |

| DeltaForce | Change in force |

| 9D ATRP | Short volatility regime |

| SUI | Scroll Utilization Index |



\---



\# Core Formulas



\## Session\_F



```text

(Latest - Open) / 14D ATR

```



Measures normalized directional impulse.



\---



\## DeltaForce



```text

Session\_F - Session\_F\_PRV

```



Measures acceleration, reversal, or directional decay.



\---



\## SUI



```text

HiLo% / 9D ATRP

```



Measures how much of the expected movement range has already been consumed.



\---



\# State Logic



```text

SUI < 0.50           → COMPRESSION

|Session\_F| > 0.80   → IMPULSE / TREND

|DeltaForce| > 1.00  → TRANSITION

SUI > 1.40           → FORCED\_EXTENSION

```



\---



\# Sample Interpretation



The sample surface captures a cross-asset inflationary stress impulse:



\- equities down

\- bonds down

\- oil up

\- dollar up

\- volatility up



This is not a classic growth scare.



It is closer to an inflationary stress / stagflationary impulse.



\---



\# Why This Matters



Most market dashboards track:

\- price

\- volatility

\- momentum



Strawberry Canyon focuses on:



```text

state + trajectory + volatility + exhaustion

```



The goal is to detect market structure, not simply market direction.



\---



\# Philosophy



Trade state, not price.



Size follows regime, not conviction.



Slope matters more than level.

