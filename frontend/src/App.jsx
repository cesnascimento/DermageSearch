import { Box, Center, Heading, Image } from '@chakra-ui/react'
import ListaProdutos from './components/listaProdutos'
import Teste from './components/accordion'
import Teste2 from './components/teste'


function App() {
  return(
  <>
  <Box bg='white' w='100vw'>
    <Heading bg='#ff8400'>
      <Image src='src/assets/logo.png' alt='dermage-logo' bg='#ff8400'></Image>
    </Heading>
      {<ListaProdutos/>}
      {/* {<Teste2/>} */}
  </Box>
  </>
  )
}

export default App
