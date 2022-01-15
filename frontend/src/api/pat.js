import axios from 'axios';

export const  patientdetail = async () => {

    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/patient/list/`);
        
        return res
        
        
    } catch(err) {
        return err;
    }
};