import React, { ReactElement, FC } from "react";
import Balances from "../components/Balances";
import Donors from "../components/Donors";

const Report: FC<any> = (): ReactElement => {
    return (
        <>
            <h2>
                Balances
            </h2>
            <Balances />
            <hr/>
            <h2>
                Donors
            </h2>
            <Donors />
        </>
    );
};

export default Report;