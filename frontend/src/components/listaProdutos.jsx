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
import data from '../json/drogariacatarinense.json'


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
                    <Center marginLeft={50}>
                        {ProdutoSelecionado && (
                            <Center>
                                <TableContainer marginTop={5}>
                                    <Table variant='simple'>
                                        <TableCaption>Dermage Products Search</TableCaption>
                                        <Thead>
                                            <Tr>
                                                <Th>Código Ean</Th>
                                                <Th>Nome</Th>
                                                <Th isNumeric>Preço</Th>
                                                <Th>Site</Th>
                                            </Tr>
                                        </Thead>
                                        {dadosDoProduto.map(produto => (
                                            <Tbody>
                                                <Tr key={produto.id}>
                                                    <Td>{produto.ean_id}</Td>
                                                    <Td>{ProdutoSelecionado.nome}</Td>
                                                    <Td>{produto.preco}</Td>
                                                    <Td><Link href={procurarLoja(produto.loja_id).site} isExternal>{procurarLoja(produto.loja_id).nome}</Link></Td>
                                                </Tr>
                                            </Tbody>
                                        ))}
                                    </Table>
                                </TableContainer>
                            </Center>
                        )}
                        <List marginTop={5}>
                            {produtos.filter(data => {
                                if (searchTerm == "") {
                                    return ""
                                } else if (data.nome.toLocaleLowerCase().includes(searchTerm.toLocaleLowerCase())) {
                                    return data
                                }
                            }).map(produto => (
                                <ListItem>
                                    {produto.nome}
                                    <Button colorScheme='blue' size='xs' margin={2} onClick={() => mostrarDadosDoProduto(produto)}>Ver preço</Button>
                                </ListItem>
                            ))}
                        </List>

                    </Center>
                </Box>
            </Center>
        </>
    )
}

export default ListaProdutos
