// Chamadas à API. Tudo passa por /api: em desenvolvimento o Vite repassa para
// o backend; no contêiner, quem repassa é o nginx (ver nginx.conf).

export type Health = {
  status: 'ok' | 'degraded'
  version: string
  environment: string
  database: 'ok' | 'error'
}

export async function getHealth(): Promise<Health> {
  const response = await fetch('/api/health')
  if (!response.ok) {
    throw new Error(`API respondeu ${response.status}`)
  }
  return response.json()
}
