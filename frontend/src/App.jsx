import { Box, Center, Heading, Image } from '@chakra-ui/react'
import ListaProdutos from './components/listaProdutos'


function App() {
  return(
  <>
  <Box bg='white'>
    <Heading bg='#ff8400'>
      <Image src='src/assets/logo.png' alt='dermage-logo' bg='#ff8400'></Image>
    </Heading>
      <ListaProdutos/>
  </Box>
  </>
  )
}

export default App
