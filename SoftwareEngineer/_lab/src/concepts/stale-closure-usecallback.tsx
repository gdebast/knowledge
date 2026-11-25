/*
 * Concept: stale closure in useCallback (why a callback prop belongs in the deps array)
 *
 * A function "closes over" the variables that exist when it is created. useCallback keeps
 * the SAME function object until a dependency changes. If that function calls a prop such
 * as onPick and onPick is not in the deps, it keeps calling the onPick from the first
 * render, even after the parent passes a new one. That old copy is the "stale closure".
 * Listing the prop in the deps rebuilds the wrapper whenever the parent passes a new function.
 *
 * Seen in: omp7_ui/apps/supply-planning/src/components/ProductLocationDetails/components/
 *   ProductLocationDetailsBoxPlanningView/ProductLocationDetailsBoxPlanningView.tsx:80-95
 * Run: npm run dev in _lab, then pick "stale-closure-usecallback".
 */
import { useCallback, useState } from 'react';

function Picker({ onPick }: { onPick: (value: string) => void }) {
  // TRY 1: change [onPick] to [] (the parent's own onPick still changes on every render).
  //   Click "A", click "Switch to v2", click "B". Predict the log line, then check.
  const handlePick = useCallback((value: string) => onPick(value), [onPick]);
  return ['A', 'B'].map(v => <button key={v} onClick={() => handlePick(v)}>{v}</button>);
}

export default function Demo() {
  const [version, setVersion] = useState('v1');
  const [log, setLog] = useState<string[]>([]);
  // A NEW function on every render that reads the CURRENT version.
  // TRY 2: wrap this in useCallback(..., [version]) and keep [] in Picker. Is it still stale? Why?
  // TRY 3: pass setLog-style logic with no captured variable (e.g. only the value). Does [] still break?
  const handlePick = (value: string) => setLog(l => [...l, `${version}: picked ${value}`]);

  return (
    <div>
      <button onClick={() => setVersion(v => (v === 'v1' ? 'v2' : 'v1'))}>Switch to {version === 'v1' ? 'v2' : 'v1'}</button>
      <p>Current version: {version}</p>
      <Picker onPick={handlePick} />
      <ul>{log.map((line, i) => <li key={i}>{line}</li>)}</ul>
    </div>
  );
}
