/*
 * Concept: Storybook story (rendering a component in isolation, in a fixed scenario)
 *
 * Storybook is a separate dev tool, not part of React. A *.stories.tsx file has a default
 * export (metadata: title, decorators = wrappers around every story) and one named export
 * per story. Each story renders the component with chosen props and fake data, and may have
 * a play() function that clicks around and asserts, which turns the story into a test.
 * This lab app is a tiny Storybook: it lists every file in src/concepts automatically.
 * Below we imitate the idea without installing Storybook.
 *
 * Seen in: omp7_ui/apps/supply-planning/src/components/BucketHorizonSelector/__stories__/
 *   BucketHorizonSelector.stories.tsx:46-115
 * Run: npm run dev in _lab, then pick "storybook-story".
 */
import { useState, type ReactNode } from 'react';

function Badge({ label, isActive }: { label: string; isActive: boolean }) {
  return <span style={{ padding: 4, background: isActive ? 'lightgreen' : 'lightgray' }}>{label}</span>;
}

// "decorator": a wrapper applied to every story (in the repo: SupplyPlanningTestingProvider).
const decorator = (story: ReactNode) => <div style={{ border: '1px dashed', padding: 8 }}>{story}</div>;

// "stories": named scenarios with fixed props. TRY 1: add a story "Long label" with a 60-char label.
const stories: Record<string, () => ReactNode> = {
  Active: () => <Badge label="Weekly" isActive />,
  Inactive: () => <Badge label="Weekly" isActive={false} />,
};

export default function Demo() {
  const [name, setName] = useState('Active');
  // TRY 2: remove decorator(...) below. What would a real story lose if its provider was missing?
  // TRY 3 (break it): make one story throw new Error('boom'). Does the whole lab page crash? Why?
  return (
    <div>
      {Object.keys(stories).map(n => <button key={n} onClick={() => setName(n)}>{n}</button>)}
      <div style={{ marginTop: 8 }}>{decorator(stories[name]())}</div>
    </div>
  );
}
