export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <section className="mx-auto flex min-h-screen max-w-6xl flex-col justify-center px-6 py-20">
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.3em] text-cyan-300">
          JobHunterGPT
        </p>

        <h1 className="max-w-4xl text-4xl font-bold tracking-tight sm:text-6xl">
          Honest AI-powered job preparation, built human-in-the-loop.
        </h1>

        <p className="mt-6 max-w-3xl text-lg leading-8 text-slate-300">
          JobHunterGPT is a local Python prototype built by Sahid Attaf in Curaçao.
          It helps prepare job application packages through keyword extraction,
          fit scoring, cover letter drafting, package review, and interview
          readiness — while keeping a human in control at every step.
        </p>

        <p className="mt-4 max-w-3xl text-sm text-slate-400">
          Built with Python, Next.js, GitHub, Vercel, and a 70-test validation suite.
        </p>

        <div className="mt-10 grid gap-4 sm:grid-cols-4">
          <Stat label="Modules" value="8+" />
          <Stat label="Tests Passing" value="70/70" />
          <Stat label="Auto-submits" value="0" />
          <Stat label="Review Mode" value="Human" />
        </div>

        <div className="mt-12 grid gap-6 lg:grid-cols-3">
          <Card
            title="How it works"
            body="The system reads a job description and resume, extracts relevant terms, scores fit, drafts a cover letter, and reviews the package before anything is used."
          />
          <Card
            title="Why it matters"
            body="It proves a responsible AI workflow: no fake claims, no automatic applications, and no private data exposed in public demos."
          />
          <Card
            title="Proof of work"
            body="The project includes a working Python CLI, a package reviewer, a demo script, learning packs, and a passing 70-test suite."
          />
        </div>

        <section className="mt-16 rounded-3xl border border-slate-800 bg-slate-900/70 p-8">
          <h2 className="text-2xl font-semibold">Builder story</h2>
          <p className="mt-4 max-w-4xl text-slate-300 leading-8">
            I&apos;m an AI systems builder based in Curaçao. Over the past five years,
            I&apos;ve been building practical AI workflows for business automation.
            My clearest example is JobHunterGPT, a human-in-the-loop Python prototype
            that prepares job application packages without removing human review.
            It handles keyword extraction, fit scoring, cover letter drafting, and
            package review before anything is used. I don&apos;t have enterprise
            platform experience yet, but I can show you the work directly — how I
            built it, how I tested it, and how I improve it.
          </p>
        </section>

        <div className="mt-10 flex flex-wrap gap-4">
          <a
            href="https://github.com/sahidattaf/jobhunter-gpt"
            className="rounded-full bg-cyan-300 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-200"
          >
            View GitHub Repo
          </a>
          <a
            href="#privacy"
            className="rounded-full border border-slate-700 px-6 py-3 font-semibold text-white transition hover:bg-slate-900"
          >
            Privacy Rules
          </a>
        </div>

        <section id="privacy" className="mt-16 border-t border-slate-800 pt-8">
          <h2 className="text-xl font-semibold">Privacy and safety rules</h2>
          <p className="mt-4 max-w-3xl text-slate-400">
            This public page does not expose private resumes, candidate profiles,
            real application packages, certificate IDs, private job descriptions,
            or application tracking data. JobHunterGPT is designed as a responsible,
            human-reviewed career preparation system.
          </p>
        </section>
      </section>
    </main>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <div className="text-3xl font-bold text-cyan-300">{value}</div>
      <div className="mt-2 text-sm text-slate-400">{label}</div>
    </div>
  );
}

function Card({ title, body }: { title: string; body: string }) {
  return (
    <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
      <h2 className="text-xl font-semibold">{title}</h2>
      <p className="mt-4 leading-7 text-slate-400">{body}</p>
    </div>
  );
}