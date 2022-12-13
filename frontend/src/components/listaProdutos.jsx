import { useState } from 'react'
import { Center, Text, Box, Input, InputGroup, InputLeftElement } from '@chakra-ui/react'
import {
    List,
    ListItem,
} from '@chakra-ui/react'
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
            <Center w='100vw' marginTop={'100px'}>
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
                            <Thead>
                                <Tr>
                                    <Td><Text as='b'>Produto</Text></Td>
                                    <Td></Td>
                                </Tr>
                            </Thead>
                            {produtos.filter(data => {
                                if (searchTerm == '') {
                                    return data
                                } else if (data.nome.toLowerCase().includes(searchTerm.toLocaleLowerCase())) {
                                    return data
                                }
                            }).map(produto => (
                                <Tbody>
                                    <Tr>

                                        <Td>{produto.nome}</Td>
                                        <Td><Button colorScheme='blue' size='xs' margin={2} onClick={() => mostrarDadosDoProduto(produto)}>Ver preço</Button></Td>
                                    </Tr>
                                    {ProdutoSelecionado && ProdutoSelecionado.ean == produto.ean && (
                                        <Center marginLeft={20}>
                                            <Table variant='unstyled' size='sm'>
                                                <TableCaption>Dermage Products Search</TableCaption>
                                                <Thead>
                                                    <Tr>
                                                        <Th>Código Ean</Th>
                                                        <Th isNumeric>Preço</Th>
                                                        <Th>Site</Th>
                                                    </Tr>
                                                </Thead>
                                                {dadosDoProduto.map(produto => (
                                                    <Tbody>
                                                        <Tr key={produto.id}>
                                                            <Td>{produto.ean_id}</Td>
                                                            <Td isNumeric>{produto.preco}</Td>
                                                            <Td><Link href={produto.link} isExternal>{procurarLoja(produto.loja_id).nome}</Link></Td>
                                                        </Tr>
                                                    </Tbody>
                                                ))}
                                            </Table>
                                        </Center>
                                    )}
                                </Tbody>
                            ))
                            }
                        </Table>
                    </TableContainer>
                </Box>
            </Center>
        </>
    )
}

export default ListaProdutos
