import {
  Badge,
  Body1,
  Caption1,
  Card,
  CardHeader,
  makeStyles,
  Spinner,
  Title2,
  tokens,
} from '@fluentui/react-components'
import { useEffect, useState } from 'react'
import { getHealth, type Health } from '../api'

// Números de exemplo: na Fase 2 eles virão da Microsoft Graph API
const exemplo = [
  { titulo: 'Dispositivos', valor: 128, detalhe: 'gerenciados pelo Intune' },
  { titulo: 'Fora de compliance', valor: 9, detalhe: 'não atendem às políticas' },
  { titulo: 'Sem política', valor: 4, detalhe: 'nenhuma política atribuída' },
  { titulo: 'Inativos', valor: 6, detalhe: 'sem sincronizar há 30 dias' },
]

const useStyles = makeStyles({
  header: { display: 'flex', alignItems: 'center', gap: tokens.spacingHorizontalM },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
    gap: tokens.spacingHorizontalL,
    marginTop: tokens.spacingVerticalXL,
  },
  valor: {
    fontSize: tokens.fontSizeHero800,
    lineHeight: tokens.lineHeightHero800,
    fontWeight: tokens.fontWeightSemibold,
  },
})

function StatusApi() {
  const [health, setHealth] = useState<Health | null>(null)
  const [erro, setErro] = useState(false)

  useEffect(() => {
    getHealth()
      .then(setHealth)
      .catch(() => setErro(true))
  }, [])

  if (erro) return <Badge color="danger">API fora do ar</Badge>
  if (!health) return <Spinner size="tiny" label="Verificando API..." />
  return (
    <Badge color={health.database === 'ok' ? 'success' : 'warning'}>
      API {health.version} · banco {health.database === 'ok' ? 'conectado' : 'com erro'}
    </Badge>
  )
}

export default function Dashboard() {
  const styles = useStyles()

  return (
    <>
      <div className={styles.header}>
        <Title2 as="h1">Dispositivos</Title2>
        <StatusApi />
      </div>
      <Caption1>Dados de exemplo — a conexão com o Intune entra na Fase 2.</Caption1>

      <div className={styles.grid}>
        {exemplo.map((item) => (
          <Card key={item.titulo}>
            <CardHeader header={<Body1>{item.titulo}</Body1>} />
            <span className={styles.valor}>{item.valor}</span>
            <Caption1>{item.detalhe}</Caption1>
          </Card>
        ))}
      </div>
    </>
  )
}
