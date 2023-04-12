import { useState, useEffect } from 'react'
import { Center, Text, Box, Input, InputGroup, InputLeftElement } from '@chakra-ui/react'
import {
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    TableCaption,
    TableContainer,
    Accordion,
    AccordionItem,
    AccordionButton,
    AccordionPanel,
} from '@chakra-ui/react'
import { Link } from '@chakra-ui/react'
import { Button } from '@chakra-ui/react'
import { BsSearch } from 'react-icons/bs'
import axios from 'axios'
import * as XLSX from 'xlsx';


function ListaProdutos() {
    const [searchTerm, setSearchTerm] = useState('')

    const [ProdutoSelecionado, setProdutoSelecionado] = useState(null)
    const [dadosDoProduto, setDadosDoProduto] = useState(null)
    const [dadosDoProdutoEncontrado, setDadosDoProdutoEncontrado] = useState([])
    const [data, setData] = useState(null);

    const produtos = data?.produtos
    const precos = data?.precos
    const lojas = data?.lojas

    function mostrarDadosDoProduto(produto) {
        setProdutoSelecionado(produto)

        let produtosEncontrados = precos.filter(preco => preco.ean_id === produto.ean)

        setDadosDoProduto(produtosEncontrados)
    }

    function procurarLoja(idLoja) {
        let nomeDaLoja = lojas.find(loja => loja.id === idLoja)
        return nomeDaLoja;
    }

    function mostrarDetalhesDoProduto(produto) {
        /* setProdutoSelecionado(produto) */

        let produtosEncontrados = precos.filter(preco => preco.ean_id === produto.ean)

        console.log('encontrados',produtosEncontrados)

        console.log('produto2',produto)

        let dadosDoProduto = produtosEncontrados.map(p => {
            let nomeDaLoja = lojas.find(loja => loja.id === p.loja_id)
            return {
                nome: produto.nome,
                ean_id: p.ean_id,
                preco: p.preco,
                link: p?.link,
                market: p?.market,
                datahora: p.datahora,
                loja: nomeDaLoja.nome
            }
        })
        console.log('dados', dadosDoProduto.flat(2))

        /* console.log('dados', dadosDoProduto.flat(2)) */

        setDadosDoProdutoEncontrado(dadosDoProdutoEncontrado => [...dadosDoProdutoEncontrado, dadosDoProduto])
    }
    console.log(dadosDoProdutoEncontrado.flat(2))

    function exportToExcel(tableData, fileName) {
        const worksheet = XLSX.utils.json_to_sheet(tableData);
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
        XLSX.writeFile(workbook, fileName + '.xlsx');
    }

    useEffect(() => {
        fetch('json/geral.json')
            .then(response => response.json())
            .then(json => setData(json))
    }, []);
    useEffect(() => {
        if (produtos) {
            produtos.forEach(element => {
                mostrarDetalhesDoProduto(element)
            });
        }
    }, [produtos]);


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
                        <Button onClick={() => exportToExcel(dadosDoProdutoEncontrado.flat(2), 'produtos')}>
                            Exportar para Excel
                        </Button>

                        <Table variant='unstyled'>
                            <Center>
                                <Accordion allowToggle>
                                    <Thead>
                                        <Tr>
                                            <Th><Text as='b'>Produto</Text></Th>
                                        </Tr>
                                    </Thead>
                                    {produtos?.filter(data => {
                                        if (searchTerm == '') {
                                            return data
                                        } else if (data.nome.toLocaleLowerCase().includes(searchTerm.toLocaleLowerCase())) {
                                            return data
                                        }
                                    }).map(produto => (
                                        <Tbody>
                                            <AccordionItem sx={{ border: 'transparent', position: 'relative', width: '100%' }}>
                                                <Tr sx={{ display: 'flex', justifyContent: 'space-between' }}>
                                                    <Td>{produto.nome}</Td>
                                                    <Td sx={{ right: 0 }}><Button colorScheme='blue' size='xs'><AccordionButton color='white' onClick={() => mostrarDadosDoProduto(produto)} _hover={{ color: 'white' }}>Ver Preço</AccordionButton></Button></Td>
                                                </Tr>
                                                {ProdutoSelecionado && ProdutoSelecionado.ean == produto.ean && (
                                                    <AccordionPanel>
                                                        <Center>
                                                            <TableContainer>
                                                                <Table variant='unstyled' size='sm'>
                                                                    <TableCaption>Dermage Products Search</TableCaption>
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
                                                                                <Td>
                                                                                    <Link href={produto.link} isExternal>{procurarLoja(produto.loja_id).nome}
                                                                                        {produto?.market !== undefined && (
                                                                                            <Text fontSize='0.8em'>Vendedor: {produto?.market}</Text>
                                                                                        )}
                                                                                    </Link>
                                                                                </Td>
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
