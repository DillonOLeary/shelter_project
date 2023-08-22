import React, {ReactElement, FC} from "react";
import {Box, Button, FilledInput, FormControl, FormHelperText, IconButton, Input, InputAdornment, InputLabel, OutlinedInput, TextField, Typography} from "@mui/material";
import { VisibilityOff, Visibility } from "@mui/icons-material";

const Donate: FC<any> = (): ReactElement => {
    return (
        <Box
            component="form"
            sx={{
            '& .MuiTextField-root': { m: 1, width: '25ch' },
            }}
            noValidate
            autoComplete="off"
        >
        <TextField
          id="donor-name"
          label="Donor Name"
        />
        <TextField
          id="donation-type"
          label="Donation Type"
        />
        <TextField
          id="units-donated"
          label="Units Donated"
        />
        <TextField
          id="donation-date"
          label="Donation Date"
        />
        <Button sx={{ m: 1 }} type="submit" variant="outlined">Submit</Button>
      </Box>
    );
};

export default Donate;