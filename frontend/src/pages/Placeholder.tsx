import { MessageBar, MessageBarBody, Title2 } from '@fluentui/react-components'

type Props = { title: string; fase: string }

// Página provisória para as abas que ainda serão construídas
export default function Placeholder({ title, fase }: Props) {
  return (
    <>
      <Title2 as="h1">{title}</Title2>
      <MessageBar intent="info" style={{ marginTop: 16 }}>
        <MessageBarBody>Esta aba será construída na {fase}.</MessageBarBody>
      </MessageBar>
    </>
  )
}
