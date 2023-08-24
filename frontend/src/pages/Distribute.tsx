import React, { ReactElement, FC, useState } from "react";
import { Box, Button, TextField } from "@mui/material";

const Distribute: FC<any> = (): ReactElement => {
    const [inputs, setInputs] = useState({
        donationType: "",
        unitsDistributed: "",
        distributionDate: ""
    });
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setInputs({ ...inputs, [name]: value });
    }
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log(`Put request with ${JSON.stringify(inputs)}`);
        submitDonation();
    }
    const submitDonation = async () => {
        const url = 'http://127.0.0.1:8000/distributions'
        const method = 'POST'

        await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(inputs)
        })
    }
    return (
        <Box
            component="form"
            onSubmit={handleSubmit}
            sx={{
                '& .MuiTextField-root': { m: 1, width: '25ch' },
            }}
            noValidate
            autoComplete="off"
        >
            <TextField
                value={inputs.donationType}
                name="donationType"
                label="Donation Type"
                onChange={handleInputChange}
            />
            <TextField
                value={inputs.unitsDistributed}
                name="unitsDistributed"
                label="Units Distributed"
                onChange={handleInputChange}
                type={"number"}
            />
            <TextField
                value={inputs.distributionDate}
                name="distributionDate"
                label="Distribution Date"
                onChange={handleInputChange}
                type={"date"}
                InputLabelProps={{
                    shrink: true,
                }}
            />
            <Button sx={{ m: 1 }} type="submit" variant="outlined">Submit</Button>
        </Box>
    );
};

export default Distribute;