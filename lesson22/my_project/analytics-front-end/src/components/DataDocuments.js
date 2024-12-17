import React from "react";
import {useQuery, gql} from '@apollo/client';

const GET_DATA_DOCUMENTS = gql`
  query {
    allDataDocuments {
        title
        description
    }
}
`;
const DataDocuments = () => {
    const {loading, error, data} = useQuery(GET_DATA_DOCUMENTS);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>Error: {error.message}</p>;
    }

    return (
        <div>
            <h1>Data Documents</h1>
            <ul>
                {data.allDataDocuments.map((doc) => (
                    <li key={doc.id}>
                        <h3>{doc.title}</h3>
                        <p>{doc.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DataDocuments;