import { useState, type ComponentType } from "react";

// Every src/concepts/*.tsx file with a default export is listed automatically.
const modules = import.meta.glob<{ default: ComponentType }>(
  "./concepts/*.tsx",
  {
    eager: true,
  },
);

const demos = Object.entries(modules)
  .map(([path, mod]) => ({
    name: path.replace("./concepts/", "").replace(".tsx", ""),
    Demo: mod.default,
  }))
  .sort((a, b) => a.name.localeCompare(b.name));

export default function App() {
  const [selected, setSelected] = useState(
    () => location.hash.slice(1) || demos[0]?.name,
  );
  const current = demos.find((d) => d.name === selected);

  function select(name: string) {
    location.hash = name;
    setSelected(name);
  }

  return (
    <div
      style={{ display: "flex", gap: 24, fontFamily: "system-ui", padding: 16 }}
    >
      <nav style={{ minWidth: 220 }}>
        <h3>Concepts</h3>
        {demos.length === 0 && <p>No lab file yet in src/concepts/.</p>}
        <ul style={{ listStyle: "none", padding: 0 }}>
          {demos.map((d) => (
            <li key={d.name}>
              <button
                onClick={() => select(d.name)}
                style={{
                  fontWeight: d.name === selected ? "bold" : "normal",
                  marginBottom: 4,
                }}
              >
                {d.name}
              </button>
            </li>
          ))}
        </ul>
      </nav>
      <main style={{ flex: 1 }}>
        {current ? (
          <>
            <h2>{current.name}</h2>
            <current.Demo key={current.name} />
          </>
        ) : null}
      </main>
    </div>
  );
}
