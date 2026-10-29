import { useEffect, useState } from 'react'

interface Plugin {
  id: string
  name: string
  description: string
  version: string
  author: string
  repository: string
  license: string
  keywords: string[]
  source: string
  lspServers?: Record<string, unknown>
}

interface MarketplaceResponse {
  plugins: Plugin[]
}

function App() {
  const [plugins, setPlugins] = useState<Plugin[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/api/marketplace')
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then((data: MarketplaceResponse) => {
        setPlugins(data.plugins || [])
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  const getIconLetter = (name: string) => name.charAt(0).toUpperCase()

  if (loading) {
    return (
      <div className="container">
        <header>
          <h1>Nexus Lens</h1>
          <p>Official Claude Code Plugin Marketplace</p>
        </header>
        <div className="loading">Loading plugins...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="container">
        <header>
          <h1>Nexus Lens</h1>
          <p>Official Claude Code Plugin Marketplace</p>
        </header>
        <div className="error">Error: {error}</div>
      </div>
    )
  }

  return (
    <div className="container">
      <header>
        <h1>Nexus Lens</h1>
        <p>Official Claude Code Plugin Marketplace</p>
      </header>
      <div className="plugin-grid">
        {plugins.map(plugin => (
          <article key={plugin.id} className="plugin-card">
            <div className="plugin-header">
              <div className="plugin-icon">{getIconLetter(plugin.name)}</div>
              <div className="plugin-info">
                <h2>{plugin.name}</h2>
                <div className="plugin-meta">
                  <span>v{plugin.version}</span>
                  <span>by {plugin.author}</span>
                </div>
              </div>
            </div>
            <p className="plugin-description">{plugin.description}</p>
            <div className="plugin-tags">
              {plugin.keywords.slice(0, 5).map(keyword => (
                <span key={keyword} className="tag">{keyword}</span>
              ))}
            </div>
            <div className="plugin-footer">
              <span>{plugin.license}</span>
              <a href={plugin.repository} target="_blank" rel="noopener noreferrer">
                View Source
              </a>
            </div>
          </article>
        ))}
        {plugins.length === 0 && (
          <div className="loading" style={{ gridColumn: '1 / -1' }}>
            No plugins found
          </div>
        )}
      </div>
    </div>
  )
}

export default App
