import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>March Madness Predictor</h1>
      <Link href="/matchup">Go to Matchup Predictor</Link>
    </div>
  );
}

