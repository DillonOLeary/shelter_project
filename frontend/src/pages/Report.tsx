import { Box } from "@mui/material";
import React, { ReactElement, FC } from "react";
import Balances from "../components/Balances";
import Donors from "../components/Donors";

const Report: FC<any> = (): ReactElement => {
    return (
        <Box sx={{ m: 1 }}>
            <h2>
                Balances
            </h2>
            <Balances />
            <h2>
                Donors
            </h2>
            <Donors />
        </Box>
    );
};

export default Report;