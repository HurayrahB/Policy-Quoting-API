import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import type { Quote } from "./types";

type QuotesState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "ready"; data: Quote[] };

const initialState: QuotesState = { status: "idle" };

export const fetchQuotes = createAsyncThunk("quotes/fetch", async () => {
  const response = await fetch("/api/quotes/");
  if (!response.ok) throw new Error(`Request failed: ${response.status}`);
  return (await response.json()) as Quote[];
});

export const createQuote = createAsyncThunk(
  "quotes/create",
  async (payload: { applicant_id: number; coverage_amount: string }) => {
    const response = await fetch("/api/quotes/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error(`Create failed: ${response.status}`);
    return (await response.json()) as Quote;
  },
);

const quotesSlice = createSlice({
  name: "quotes",
  initialState: initialState as QuotesState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchQuotes.pending, () => ({ status: "loading" }) as QuotesState)
      .addCase(
        fetchQuotes.fulfilled,
        (_state, action) =>
          ({ status: "ready", data: action.payload }) as QuotesState,
      )
      .addCase(
        fetchQuotes.rejected,
        (_state, action) =>
          ({
            status: "error",
            message: action.error.message ?? "Unknown error",
          }) as QuotesState,
      )
      .addCase(createQuote.fulfilled, (state, action) => {
        if (state.status === "ready") {
          state.data.push(action.payload);
        }
      });
  },
});

export default quotesSlice.reducer;