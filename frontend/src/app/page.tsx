"use client";
import useSWRMutation from 'swr/mutation';
import useSWR from 'swr';
 
const updateExample = async (url: string, { arg }: { arg: string }) => {
  await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ data: arg })
  })
    .then(res => res.json())
    .then(json => console.log(`button press data response: "${Object.values(json["data"]["received_body"] || {})}"`));
}

const fetcher = (url: string) => fetch(url).then(res => res.json());

export default function Home() {
  // Fetcher implementation.
  // The extra argument will be passed via the `arg` property of the 2nd parameter.
  // In the example below, `arg` will be `'trigger data arg'`
  const options = {};
  // A useSWR + mutate like API, but it will not start the request automatically.
  const { data: data3, trigger } = useSWRMutation('http://localhost:5000/api/v1/examples', updateExample, options);
  console.log(`button press data: "${Object.values(data3 || {})}"`);
  
  const { data } = useSWR('http://localhost:5000/api/v1/examples', fetcher);
  const { data: data2 } = useSWR('http://localhost:5000/api/v1/examples/1', fetcher);
  console.log(`get examples "${Object.values(data || {})}"`);
  console.log(`get example "${Object.values(data2 || {})}"`);
  
  return (<div>

    <button onClick={() => {
      // Trigger `updateExample`.
      trigger("trigger data arg");
    }}>Update Example</button>
  </div>);
}
