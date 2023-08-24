import React, { ReactElement, FC, useState, useEffect } from "react";
import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";

type Row = {
    category: string;
    quantity: number;
}

const Report: FC<any> = (): ReactElement => {
    const [rows, setRows] = useState<Row[]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/balances")
            .then(response => response.json())
            .then(json => setRows(json))
    })

    return (
        <TableContainer sx={{ maxWidth: 500 }} component={Paper}>
            <Table sx={{ minWidth: 200 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell sx={{ fontWeight: 'bold' }}>Category</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }} align="right">Balance</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        <TableRow
                            key={row.category}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {row.category}
                            </TableCell>
                            <TableCell align="right">{row.quantity}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default Report;