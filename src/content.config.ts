import { defineCollection, z } from "astro:content";

const pages = defineCollection({
  type: "content",
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
