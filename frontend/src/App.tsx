import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "./store";
import { fetchQuotes, createQuote } from "./quotesSlice";

export default function App() {
  const dispatch = useDispatch<AppDispatch>();
  const quotes = useSelector((state: RootState) => state.quotes);

  const [applicantId, setApplicantId] = useState("");
  const [coverage, setCoverage] = useState("");

  useEffect(() => {
    dispatch(fetchQuotes());
  }, [dispatch]);

  const submit = () => {
    dispatch(
      createQuote({
        applicant_id: Number(applicantId),
        coverage_amount: coverage,
      }),
    );
  };

  return (
    <div style={{ padding: 24, fontFamily: "sans-serif" }}>
      <h1>Quotes</h1>

      <div style={{ marginBottom: 24 }}>
        <input
          value={applicantId}
          onChange={(e) => setApplicantId(e.target.value)}
          placeholder="Applicant ID"
        />
        <input
          value={coverage}
          onChange={(e) => setCoverage(e.target.value)}
          placeholder="Coverage amount"
        />
        <button onClick={submit}>Create</button>
      </div>

      {quotes.status === "loading" && <p>Loading...</p>}
      {quotes.status === "error" && <p>Error: {quotes.message}</p>}
      {quotes.status === "ready" && (
        <table>
          <tbody>
            {quotes.data.map((q) => (
              <tr key={q.id}>
                <td>{q.id}</td>
                <td>{q.applicant.name}</td>
                <td>{q.applicant.province}</td>
                <td>{q.coverage_amount}</td>
                <td>{q.premium ?? "unpriced"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}