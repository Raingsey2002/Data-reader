import { syncData } from '../../../../scripts/sync-data.mjs';

export async function GET() {
  try {
    // Ensure environment variables are set for the sync script
    // In Vercel, these should be configured as environment variables for the project.
    if (!process.env.DATABASE_URL || 
        !process.env.GOOGLE_SHEET_URL_2025 || 
        !process.env.GOOGLE_SHEET_URL_2024 || 
        !process.env.GOOGLE_SHEET_URL_2023 || 
        !process.env.GOOGLE_SHEET_URL_2022 || 
        !process.env.GOOGLE_SHEET_URL_2021) {
      throw new Error("Missing one or more required environment variables for data synchronization.");
    }

    await syncData();
    return new Response('Data synchronization initiated successfully.', { status: 200 });
  } catch (error: unknown) {
    console.error('Error during data synchronization via cron job:', error);
    const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred';
    return new Response(`Data synchronization failed: ${errorMessage}`, { status: 500 });
  }
}
