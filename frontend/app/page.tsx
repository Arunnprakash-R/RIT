import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function DashboardPage() {
  return (
    <div className="container mx-auto p-4 md:p-8">
      <h1 className="text-3xl font-bold mb-6">Live Dashboard</h1>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {/* This is where metric cards would be dynamically generated */}
        <Card>
          <CardHeader>
            <CardTitle>Total Calls Today</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">1,250</p>
            <p className="text-xs text-muted-foreground">+20% from yesterday</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Avg. Resolution Time</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">180s</p>
            <p className="text-xs text-muted-foreground">-15s from yesterday</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Escalation Rate</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">21.6%</p>
            <p className="text-xs text-muted-foreground">+2% from yesterday</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>CSAT</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">4.5/5</p>
            <p className="text-xs text-muted-foreground">Stable</p>
          </CardContent>
        </Card>
      </div>

      <div className="mt-8">
        <h2 className="text-2xl font-bold mb-4">Live Interactions</h2>
        {/* This would be a real-time feed of calls */}
        <div className="p-4 border rounded-lg">
          <p className="text-muted-foreground">Live feed component placeholder...</p>
          <p>// TODO: Implement a component to show live call transcripts</p>
        </div>
      </div>
    </div>
  );
}
