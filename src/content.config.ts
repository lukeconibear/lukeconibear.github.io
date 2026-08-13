import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const pages = defineCollection({
  loader: glob({
    base: "./src/content/pages",
    pattern: "**/*.{md,mdx}"
  }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    summary: z.string().optional(),
    section: z.enum(["home", "software", "atmospheric_science"]),
    order: z.number().int().nonnegative().optional()
  })
});

export const collections = {
  pages
};
