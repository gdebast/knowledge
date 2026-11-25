/*
 * Concept: controlled component (value + onChange props, no own state)
 *
 * A controlled component does not store the value it displays. The parent passes the
 * current value as a prop and a callback to ask for a change. The parent owns the state
 * (lifting the state up), so the SAME component can be reused by parents that keep the
 * state in different places: a plain useState, a custom hook, a page config...
 *
 * Seen in: omp7_ui/apps/supply-planning/src/components/BucketHorizonSelector/BucketHorizonSelector.tsx:9-14
 *   (selectedBucketHorizonId + onSelectedBucketHorizonIdChange), used by 3 different parents.
 * Run: npm run dev in _lab, then pick "controlled-component".
 */
import { useState } from "react";

type HorizonPickerProps = {
  value: string | null;
  onValueChange: (value: string | null) => void;
};

function HorizonPicker({ value, onValueChange }: HorizonPickerProps) {
  return (
    <select
      value={value ?? ""}
      onChange={(e) => onValueChange(e.target.value || null)}
    >
      <option value="">(global)</option>
      <option value="Daily">Daily</option>
      <option value="Weekly">Weekly</option>
    </select>
  );
}

export default function Demo() {
  const [horizon, setHorizon] = useState<string | null>("Weekly");
  // TRY 1: replace setHorizon with () => {} (as many repo stories do). Can you still change
  //   the selection? Predict, then run. Who really decides what is displayed?
  // TRY 2: pass onValueChange={v => setHorizon(v === 'Daily' ? 'Weekly' : v)}. The parent can
  //   veto a choice: what does the user see when picking Daily?
  // TRY 3: render a second <HorizonPicker> with the same props. Why do both always agree?
  return (
    <div>
      <HorizonPicker value={horizon} onValueChange={setHorizon} />
      <p>Parent state: {horizon ?? "null"}</p>
    </div>
  );
}
