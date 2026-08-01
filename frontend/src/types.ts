export interface Applicant {
    id: number;
    name: string;
    province: string;
    date_of_birth: string;
}

export interface Quote {
    id: number;
    applicant: Applicant;
    coverage_amount: string; // drf serialized DecimalField to string (due to float precision)
    premium: string | null;
    status: "draft" | "bound" | "expired";
    created_at: string;
}