import React, { ReactElement, FC, useState } from "react";
import { Box, Button, TextField } from "@mui/material";

const Donate: FC<any> = (): ReactElement => {
    const [inputs, setInputs] = useState({
        donorName: "",
        donationType: "",
        unitsDonated: "",
        donationDate: ""
    });
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setInputs({ ...inputs, [name]: value });
    }
    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log(inputs);
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
                value={inputs.donorName}
                name="donorName"
                label="Donor Name"
                onChange={handleInputChange}
            />
            <TextField
                value={inputs.donationType}
                name="donationType"
                label="Donation Type"
                onChange={handleInputChange}
            />
            <TextField
                value={inputs.unitsDonated}
                name="unitsDonated"
                label="Units Donated"
                onChange={handleInputChange}
                type={"number"}
            />
            <TextField
                value={inputs.donationDate}
                name="donationDate"
                label="Donation Date"
                onChange={handleInputChange}
            />
            <Button sx={{ m: 1 }} type="submit" variant="outlined">Submit</Button>
        </Box>
    );
};

export default Donate;