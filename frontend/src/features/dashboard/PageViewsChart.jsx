import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from 'recharts';


const PageViewsChart = ({
  data
}) => {

  const chartData = data.map(
    (page) => ({
      page: page.payload__page,
      views: page.view_count
    })
  );

  return (

    <div
      style={{
        marginTop: '30px'
      }}
    >

      <h3>
        Page Views Analytics
      </h3>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={chartData}>

          <XAxis dataKey="page" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="views" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
};

export default PageViewsChart;
