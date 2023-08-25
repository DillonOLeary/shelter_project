import { TableContainer, Paper, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';
import React, { FC, ReactElement, useEffect, useState } from 'react'

type Row = {
  donor: string;
  record: string;
}

const Donors: FC<any> = (): ReactElement => {
  const [rows, setRows] = useState<Row[]>([]);

  useEffect(() => {
      fetch("http://127.0.0.1:8000/donor-records")
          .then(response => response.json())
          .then(json => setRows(json))
  }, [])

  return (
      <TableContainer sx={{ maxWidth: 500 }} component={Paper}>
          <Table sx={{ minWidth: 200 }} aria-label="simple table">
              <TableHead>
                  <TableRow>
                      <TableCell sx={{ fontWeight: 'bold' }}>Donor</TableCell>
                      <TableCell sx={{ fontWeight: 'bold' }} align="right">Donor's Balances</TableCell>
                  </TableRow>
              </TableHead>
              <TableBody>
                  {rows.map((row) => (
                      <TableRow
                          key={row.donor}
                          sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                      >
                          <TableCell component="th" scope="row">
                              {row.donor}
                          </TableCell>
                          <TableCell align="right">{JSON.stringify(row.record)}</TableCell>
                      </TableRow>
                  ))}
              </TableBody>
          </Table>
      </TableContainer>
  );
};

export default Donors