import { useState } from 'react'
import { Center, Text, Box, Input, InputGroup, InputLeftElement, border } from '@chakra-ui/react'
import {
    Table,
    Thead,
    Tbody,
    Tfoot,
    Tr,
    Th,
    Td,
    TableCaption,
    TableContainer,
    Accordion,
    AccordionItem,
    AccordionButton,
    AccordionPanel,
    AccordionIcon,
} from '@chakra-ui/react'
import { Link } from '@chakra-ui/react'
import { Button, ButtonGroup } from '@chakra-ui/react'
import { BsSearch } from 'react-icons/bs'
import data from '../json/geral.json'


function ListaProdutos() {
    const [searchTerm, setSearchTerm] = useState('')

    const [ProdutoSelecionado, setProdutoSelecionado] = useState(null);
    const [dadosDoProduto, setDadosDoProduto] = useState(null);

    const produtos = data.produtos
    const precos = data.precos
    const lojas = data.lojas

    function mostrarDadosDoProduto(produto) {
        setProdutoSelecionado(produto)

        let produtosEncontrados = precos.filter(preco => preco.ean_id === produto.ean)

        setDadosDoProduto(produtosEncontrados)
    }

    function procurarLoja(idLoja) {
        let nomeDaLoja = lojas.find(loja => loja.id === idLoja);
        return nomeDaLoja;
    }

    return (
        <>
            <Center>
                <Box>
                    <Text fontSize='5xl' align='center'>Dermage Product Search</Text>
                    <InputGroup marginTop={10}>
                        <InputLeftElement m='1' pointerEvents='none' children={<BsSearch />} />
                        <Input size='lg' bg='white' placeholder='Digite o nome do produto'
                            _placeholder={{ opacity: 0.6, color: 'black' }}
                            onChange={e => { setSearchTerm(e.target.value) }}>
                        </Input>
                    </InputGroup>
                    <TableContainer>
                        <Table variant='unstyled'>
                            <TableCaption>Dermage Products Search</TableCaption>
                            <Center>
                                <Accordion allowToggle>
                                    <Thead>
                                        <Tr>
                                            <Th><Text as='b'>Produto</Text></Th>
                                        </Tr>
                                    </Thead>
                                        {produtos.filter(data => {
                                            if (searchTerm == '') {
                                                return data
                                            } else if (data.nome.toLocaleLowerCase().includes(searchTerm.toLocaleLowerCase())) {
                                                return data
                                            }
                                        }).map(produto => (
                                            <Tbody>
                                                <AccordionItem sx={{ border: 'transparent', position: 'relative'}}>
                                                    <Tr>
                                                        <Td>{produto.nome}</Td>
                                                        <Td sx={{position: 'absolute', right: 0}}><Button colorScheme='blue' size='xs'><AccordionButton color='white' onClick={() => mostrarDadosDoProduto(produto)} _hover={{color:'white'}}>Ver Preço</AccordionButton></Button></Td>
                                                    </Tr>
                                                    {ProdutoSelecionado && ProdutoSelecionado.ean == produto.ean && (
                                                        <AccordionPanel>
                                                            <Center>
                                                                <TableContainer>
                                                                    <Table variant='unstyled' size='sm'>
                                                                        <Thead>
                                                                            <Tr>
                                                                                <Th>Código EAN</Th>
                                                                                <Th isNumeric>Preço</Th>
                                                                                <Th>Site</Th>
                                                                                <Th>Data/Hora</Th>
                                                                            </Tr>
                                                                        </Thead>
                                                                        {dadosDoProduto.map(produto => (
                                                                            <Tbody>
                                                                                <Tr>
                                                                                    <Td>{produto.ean_id}</Td>
                                                                                    <Td isNumeric>{produto.preco}</Td>
                                                                                    <Td><Link href={produto.link} isExternal>{procurarLoja(produto.loja_id).nome} <Text fontSize='0.8em'>{produto?.market}</Text></Link></Td>
                                                                                    <Td>{produto.datahora}</Td>
                                                                                </Tr>
                                                                            </Tbody>
                                                                        ))}
                                                                    </Table>
                                                                </TableContainer>
                                                            </Center>
                                                        </AccordionPanel>
                                                    )}
                                                </AccordionItem>
                                            </Tbody>
                                        ))}
                                </Accordion>
                            </Center>
                        </Table>
                    </TableContainer>
                </Box >
            </Center >
        </>
    )
}

export default ListaProdutos
