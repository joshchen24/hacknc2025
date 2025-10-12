export async function fetchSuggestions(matrix: boolean[][]): Promise<boolean[][]> {
  const r = await fetch("/api/suggest", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ matrix }),
  });
  if (!r.ok) throw new Error(`Suggest failed: ${r.status}`);
  const data = await r.json();
  return data.suggestions as boolean[][];
}


