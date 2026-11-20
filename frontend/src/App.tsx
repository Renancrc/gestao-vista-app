import {
  makeStyles,
  NavDrawer,
  NavDrawerBody,
  NavItem,
  Text,
  tokens,
} from '@fluentui/react-components'
import {
  Board24Regular,
  PeopleTeam24Regular,
  Settings24Regular,
  ShieldCheckmark24Regular,
} from '@fluentui/react-icons'
import { Route, Routes, useLocation, useNavigate } from 'react-router'
import Dashboard from './pages/Dashboard'
import Placeholder from './pages/Placeholder'

// Menu lateral: cada item é uma aba do painel
const menu = [
  { path: '/', label: 'Dispositivos', icon: <Board24Regular /> },
  { path: '/seguranca', label: 'Segurança', icon: <ShieldCheckmark24Regular /> },
  { path: '/entra-id', label: 'Entra ID', icon: <PeopleTeam24Regular /> },
  { path: '/configuracoes', label: 'Configurações', icon: <Settings24Regular /> },
]

const useStyles = makeStyles({
  shell: { display: 'flex', flexDirection: 'column', height: '100vh' },
  header: {
    display: 'flex',
    alignItems: 'center',
    gap: tokens.spacingHorizontalM,
    height: '48px',
    paddingInline: tokens.spacingHorizontalL,
    backgroundColor: tokens.colorBrandBackground,
    color: tokens.colorNeutralForegroundOnBrand,
  },
  body: { display: 'flex', flex: 1, minHeight: 0 },
  content: {
    flex: 1,
    overflowY: 'auto',
    padding: tokens.spacingHorizontalXXL,
    backgroundColor: tokens.colorNeutralBackground2,
  },
})

export default function App() {
  const styles = useStyles()
  const location = useLocation()
  const navigate = useNavigate()

  return (
    <div className={styles.shell}>
      <header className={styles.header}>
        <Text weight="semibold" size={400}>
          Gestão à Vista Microsoft
        </Text>
        <Text size={200}>Intune + Entra ID</Text>
      </header>

      <div className={styles.body}>
        <NavDrawer
          open
          type="inline"
          selectedValue={location.pathname}
          onNavItemSelect={(_, data) => navigate(String(data.value))}
        >
          <NavDrawerBody>
            {menu.map((item) => (
              <NavItem key={item.path} value={item.path} icon={item.icon}>
                {item.label}
              </NavItem>
            ))}
          </NavDrawerBody>
        </NavDrawer>

        <main className={styles.content}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route
              path="/seguranca"
              element={<Placeholder title="Segurança" fase="Fase 5" />}
            />
            <Route path="/entra-id" element={<Placeholder title="Entra ID" fase="Fase 4" />} />
            <Route
              path="/configuracoes"
              element={<Placeholder title="Configurações" fase="Fase 4" />}
            />
          </Routes>
        </main>
      </div>
    </div>
  )
}
