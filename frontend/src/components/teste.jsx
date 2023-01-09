import { useState, useEffect } from "react"
import axios from 'axios'

export default function teste() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('json/geral.json')
            .then(response => response.json())
            .then(json => setData(json))
    }, []);


    console.log(data?.produtos)



    return (
        <div>
           
        </div>
    )

}