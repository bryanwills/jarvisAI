import { NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function POST(request: Request) {
  try {
    const { prompt } = await request.json();

    // Here you would add your actual LLM integration logic
    const mockResponse = `Processed: ${prompt}`;

    const interaction = await prisma.lLMInteraction.create({
      data: {
        prompt,
        response: mockResponse,
      },
    });

    return NextResponse.json(interaction);
  } catch (error) {
    return NextResponse.json(
      { error: "Internal Server Error" },
      { status: 500 },
    );
  }
}
